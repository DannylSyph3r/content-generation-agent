"""
Smart Routing Pipeline
Hybrid approach: LLM routing decisions + Python conditional execution
"""
import asyncio
import uuid
from typing import Dict, List, Any
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
from src.agents.quality import quality_synthesizer
from src.utils.parsing import parse_routing_decision, build_clarification_message
from src.utils.runners import run_single_agent


async def create_smart_routed_content(request: str) -> str:
    """
    Main smart routing pipeline with conditional execution.
    
    Steps:
    1. Smart routing decision (1 API call)
    2. Parse decision and check for clarification needs
    3. Research enhancement for selected platforms (1 API call) 
    4. Conditional content generation (N API calls based on selection)
    5. Final synthesis with quality assessment (1 API call)
    """
    try:
        print(f"\n>> Processing Request: {request}")
        print("   Smart Routing Pipeline Active")
        print("   Features: Platform Selection → Conditional Execution → Quality Optimization")
        print("-" * 60)
        
        # Step 1: Smart Routing Decision
        print("\n>> SMART ROUTING - Analyzing request and selecting platforms")
        
        user_id = "content_creator"
        session_id = str(uuid.uuid4())
        
        routing_result = await run_single_agent(
            smart_router, user_id, session_id, request
        )
        
        # Add rate limiting delay
        await asyncio.sleep(4)
        
        # Step 2: Parse Routing Decision
        print(">> DECISION PARSING - Processing platform selection")
        
        routing_decision = parse_routing_decision(routing_result)
        selected_platforms = routing_decision.get("selected_platforms", [])
        confidence = routing_decision.get("confidence", "LOW")
        clarification_needed = routing_decision.get("clarification_needed", False)
        content_focus = routing_decision.get("content_focus", "Unknown")
        
        print(f"   - Selected Platforms: {selected_platforms}")
        print(f"   - Confidence: {confidence}")
        print(f"   - Content Focus: {content_focus}")
        
        # Step 3: Handle Clarification Needs
        if clarification_needed or confidence == "LOW" or not selected_platforms:
            print("\n>> CLARIFICATION NEEDED - Request unclear")
            clarification_msg = build_clarification_message()
            return f"\n**CLARIFICATION NEEDED**\n\n{clarification_msg}"
        
        print(f"\n>> ROUTING CONFIRMED - Proceeding with {len(selected_platforms)} platform(s)")
        
        # Step 4: Research Enhancement
        print("\n>> RESEARCH ENHANCEMENT - Gathering current information")
        research_prompt = f"Research current information about: {content_focus}"
        
        research_data = await run_single_agent(
            research_agent, user_id, session_id, research_prompt
        )
        
        await asyncio.sleep(4)
        
        # Step 5: Conditional Content Generation
        print("\n>> CONTENT GENERATION - Creating platform-specific content")
        print(f"   Generating content for: {', '.join(selected_platforms)}")
        
        platform_agents = {
            "x_twitter": x_content_specialist,
            "linkedin": linkedin_content_specialist,
            "instagram": instagram_content_specialist,
            "blog": blog_content_specialist
        }
        
        generated_content = {}
        failed_platforms = []
        
        for platform in selected_platforms:
            if platform in platform_agents:
                print(f"   - Generating {platform} content...")
                agent = platform_agents[platform]
                
                try:
                    content_prompt = f"Content Focus: {content_focus}\\nResearch Data: {research_data}"
                    content = await run_single_agent(
                        agent, user_id, session_id, content_prompt
                    )
                    generated_content[platform] = content
                    
                    # Rate limiting between platforms
                    await asyncio.sleep(7)
                    
                except Exception as e:
                    print(f"   ! Failed to generate {platform} content: {e}")
                    failed_platforms.append(platform)
            else:
                print(f"   ! Unknown platform: {platform}")
                failed_platforms.append(platform)
        
        # Step 6: Final Synthesis
        print("\n>> FINAL SYNTHESIS - Packaging and quality assessment")
        
        # Format content for synthesis
        content_package = f"""
ROUTING DECISION:
- Selected Platforms: {selected_platforms}
- Confidence: {confidence}
- Content Focus: {content_focus}

RESEARCH INSIGHTS:
{research_data}

GENERATED CONTENT:
"""
        for platform, content in generated_content.items():
            content_package += f"\\n**{platform.upper()}:**\\n{content}\\n"
        
        if failed_platforms:
            content_package += f"\\n**FAILED PLATFORMS:** {', '.join(failed_platforms)}\\n"
        
        # Final quality synthesis
        final_result = await run_single_agent(
            quality_synthesizer, user_id, session_id, content_package
        )
        
        # Add failure notice if any platforms failed
        if failed_platforms:
            failure_notice = f"\\n\\n**Note:** Content generation failed for: {', '.join(failed_platforms)}"
            final_result += failure_notice
        
        return final_result
        
    except Exception as e:
        error_msg = f"\\nError in smart routing pipeline: {str(e)}"
        print(error_msg)
        return error_msg