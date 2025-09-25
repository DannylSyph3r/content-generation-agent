"""
Smart Routing Pipeline
Hybrid approach: LLM routing decisions + Python conditional execution + Quality feedback loop
"""
import asyncio
import uuid
from typing import Dict, List, Any, Tuple
from google.adk.agents import LlmAgent
from google.adk.runners import InMemoryRunner
from google.genai import types

from src.agents.routing import smart_router
from src.agents.content import (
    x_content_specialist,
    linkedin_content_specialist,
    instagram_content_specialist,
    blog_content_specialist
)
from src.agents.research import research_agent
from src.agents.quality import quality_synthesizer, quality_checker, content_regenerator
from src.utils.parsing import parse_routing_decision, build_clarification_message
from src.utils.runners import run_single_agent
from src.utils.quality import (
    parse_quality_score, 
    is_score_acceptable, 
    should_retry_generation,
    format_regeneration_prompt,
    format_final_result_with_attempts
)
from src.config import QUALITY_SCORE_THRESHOLD, MAX_QUALITY_ATTEMPTS, RATE_LIMIT_DELAYS


async def regenerate_content_with_feedback(
    platform: str, 
    original_content: str, 
    quality_feedback: str, 
    research_data: str, 
    user_id: str, 
    session_id: str,
    attempt: int
) -> str:
    """
    Regenerate content for a specific platform based on quality feedback.
    
    Args:
        platform: Platform name (x_twitter, linkedin, instagram, blog)
        original_content: The original content that needs improvement
        quality_feedback: Quality assessment feedback
        research_data: Research data to include in regeneration
        user_id: User identifier
        session_id: Session identifier
        attempt: Current attempt number
        
    Returns:
        Regenerated content for the platform
    """
    try:
        # Map platform to specialist (same mapping as original)
        platform_specialists = {
            "x_twitter": x_content_specialist,
            "linkedin": linkedin_content_specialist, 
            "instagram": instagram_content_specialist,
            "blog": blog_content_specialist
        }
        
        specialist = platform_specialists.get(platform)
        if not specialist:
            print(f"Warning: No specialist found for platform {platform}")
            return original_content
        
        # Create regeneration prompt
        regeneration_prompt = format_regeneration_prompt(
            original_content, quality_feedback, attempt
        )
        
        # Add research data context
        full_prompt = f"""RESEARCH DATA:
{research_data}

{regeneration_prompt}"""
        
        # Generate improved content
        improved_content = await run_single_agent(
            specialist, user_id, session_id, full_prompt
        )
        
        return improved_content
        
    except Exception as e:
        print(f"Error regenerating content for {platform}: {e}")
        return original_content


async def quality_feedback_loop(
    generated_content: Dict[str, str],
    research_data: str,
    user_id: str, 
    session_id: str,
    max_attempts: int = MAX_QUALITY_ATTEMPTS,
    score_threshold: float = QUALITY_SCORE_THRESHOLD
) -> Tuple[Dict[str, str], List[float], int]:
    """
    Quality feedback loop that regenerates content until acceptable or max attempts reached.
    
    Args:
        generated_content: Dict of platform -> content
        research_data: Research data for context
        user_id: User identifier  
        session_id: Session identifier
        max_attempts: Maximum regeneration attempts (from settings)
        score_threshold: Minimum acceptable quality score (from settings)
        
    Returns:
        Tuple of (final_content_dict, scores_history, attempts_made)
    """
    current_content = generated_content.copy()
    scores_history = []
    attempt = 1
    
    while attempt <= max_attempts:
        print(f"\n>> QUALITY ASSESSMENT - Attempt {attempt}/{max_attempts}")
        
        # Format content for quality assessment
        content_package = "GENERATED CONTENT FOR ASSESSMENT:\n"
        for platform, content in current_content.items():
            content_package += f"\n**{platform.upper()}:**\n{content}\n"
        
        # Assess quality
        quality_result = await run_single_agent(
            quality_checker, user_id, session_id, content_package
        )
        
        # Parse score
        score = parse_quality_score(quality_result)
        scores_history.append(score)
        
        print(f"   Quality Score: {score:.1f}/10")
        
        # Check if acceptable or max attempts reached
        if is_score_acceptable(score, score_threshold):
            print(f"   ✅ Content approved! Score {score:.1f} meets threshold {score_threshold}")
            break
            
        if attempt >= max_attempts:
            print(f"   ⚠️ Max attempts reached. Final score: {score:.1f}")
            break
            
        # Regenerate content for next attempt
        print(f"   🔄 Score {score:.1f} below threshold {score_threshold}. Regenerating content...")
        
        # Add delay between attempts
        await asyncio.sleep(2)
        
        improved_content = {}
        for platform, content in current_content.items():
            try:
                improved = await regenerate_content_with_feedback(
                    platform, content, quality_result, research_data, 
                    user_id, session_id, attempt
                )
                improved_content[platform] = improved
                await asyncio.sleep(1)  # Rate limiting between platforms
                
            except Exception as e:
                print(f"   Error improving {platform} content: {e}")
                improved_content[platform] = content  # Keep original on error
        
        current_content = improved_content
        attempt += 1
    
    return current_content, scores_history, attempt - 1


async def create_smart_routed_content(request: str) -> str:
    """
    Main smart routing pipeline with conditional execution and quality feedback loop.
    
    Steps:
    1. Smart routing decision (1 API call)
    2. Parse decision and check for clarification needs
    3. Research enhancement for selected platforms (1 API call) 
    4. Conditional content generation (N API calls based on selection)
    5. Quality feedback loop with regeneration (up to MAX_QUALITY_ATTEMPTS iterations)
    6. Final synthesis with quality assessment (1 API call)
    """
    try:
        print(f"\n>> Processing Request: {request}")
        print("   Smart Routing Pipeline Active")
        print("   Features: Platform Selection → Conditional Execution → Quality Feedback Loop")
        print("-" * 60)
        
        # Step 1: Smart Routing Decision
        print("\n>> SMART ROUTING - Analyzing request and selecting platforms")
        
        user_id = "content_creator"
        session_id = str(uuid.uuid4())
        
        routing_result = await run_single_agent(
            smart_router, user_id, session_id, request
        )
        
        # Rate limiting after routing
        await asyncio.sleep(RATE_LIMIT_DELAYS["after_routing"])
        
        # Step 2: Parse Routing Decision
        print(">> DECISION PARSING - Processing platform selection")
        
        routing_decision = parse_routing_decision(routing_result)
        selected_platforms = routing_decision.get("selected_platforms", [])
        confidence = routing_decision.get("confidence", "LOW")
        clarification_needed = routing_decision.get("clarification_needed", False)
        content_focus = routing_decision.get("content_focus", "Unknown")
        
        print(f"   Selected Platforms: {selected_platforms}")
        print(f"   Confidence: {confidence}")
        
        # Handle clarification needs
        if clarification_needed or not selected_platforms:
            print("   ⚠️ Clarification needed or no platforms selected")
            return build_clarification_message()
        
        # Step 3: Research Enhancement
        print("\n>> RESEARCH ENHANCEMENT - Gathering current information")
        
        research_prompt = f"""Research current trends and information for: {request}
        
        Target platforms: {', '.join(selected_platforms)}
        Content focus: {content_focus}
        
        Provide relevant, current data that would enhance content creation for these platforms."""
        
        research_data = await run_single_agent(
            research_agent, user_id, session_id, research_prompt
        )
        
        await asyncio.sleep(RATE_LIMIT_DELAYS["after_research"])
        
        # Step 4: Conditional Content Generation
        print("\n>> CONTENT GENERATION - Creating platform-specific content")
        
        # Map platforms to specialists
        platform_specialists = {
            "x_twitter": x_content_specialist,
            "linkedin": linkedin_content_specialist,
            "instagram": instagram_content_specialist,
            "blog": blog_content_specialist
        }
        
        generated_content = {}
        failed_platforms = []
        
        for platform in selected_platforms:
            if platform in platform_specialists:
                try:
                    print(f"   → Generating {platform} content")
                    
                    # Create enhanced prompt with research
                    enhanced_prompt = f"""RESEARCH DATA:
{research_data}

ORIGINAL REQUEST: {request}

Create {platform} content that incorporates the research insights naturally while maintaining platform best practices and authentic voice."""
                    
                    content = await run_single_agent(
                        platform_specialists[platform], user_id, session_id, enhanced_prompt
                    )
                    generated_content[platform] = content
                    
                    await asyncio.sleep(RATE_LIMIT_DELAYS["between_platforms"])
                    
                except Exception as e:
                    print(f"   ! Failed to generate {platform} content: {e}")
                    failed_platforms.append(platform)
            else:
                print(f"   ! Unknown platform: {platform}")
                failed_platforms.append(platform)
        
        if not generated_content:
            return "Error: Could not generate content for any selected platforms."
        
        # Step 5: Quality Feedback Loop
        print("\n>> QUALITY FEEDBACK LOOP - Iterative improvement")
        
        final_content, scores_history, attempts_made = await quality_feedback_loop(
            generated_content, research_data, user_id, session_id
        )
        
        # Step 6: Final Synthesis
        print("\n>> FINAL SYNTHESIS - Packaging optimized content")
        
        # Format content for synthesis
        content_package = f"""
ROUTING DECISION:
- Selected Platforms: {selected_platforms}
- Confidence: {confidence}
- Content Focus: {content_focus}

RESEARCH INSIGHTS:
{research_data}

QUALITY-OPTIMIZED CONTENT:
"""
        for platform, content in final_content.items():
            content_package += f"\n**{platform.upper()}:**\n{content}\n"
        
        if failed_platforms:
            content_package += f"\n**FAILED PLATFORMS:** {', '.join(failed_platforms)}\n"
        
        # Use enhanced final result formatting with quality tracking
        final_result = format_final_result_with_attempts(
            content_package, scores_history, attempts_made
        )
        
        # Add failure notice if any platforms failed
        if failed_platforms:
            failure_notice = f"\n\n**Note:** Content generation failed for: {', '.join(failed_platforms)}"
            final_result += failure_notice
        
        return final_result
        
    except Exception as e:
        error_msg = f"\nError in smart routing pipeline: {str(e)}"
        print(error_msg)
        return error_msg