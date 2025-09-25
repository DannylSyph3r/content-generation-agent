"""
Parsing utilities for Smart Routing Pipeline
JSON parsing, decision handling, and message building
"""
import json
from typing import Dict, List, Any
from google.adk.agents import LlmAgent


def parse_routing_decision(routing_json: str) -> Dict[str, Any]:
    """
    Parse routing decision JSON and handle potential formatting issues.
    
    Args:
        routing_json: JSON string from routing agent
        
    Returns:
        Dict with routing decision or default error state
    """
    try:
        # Clean the JSON string
        cleaned_json = routing_json.strip()
        if cleaned_json.startswith('```json'):
            cleaned_json = cleaned_json.replace('```json', '').replace('```', '').strip()
        
        decision = json.loads(cleaned_json)
        return decision
    except json.JSONDecodeError as e:
        print(f"Warning: Failed to parse routing decision: {e}")
        return {
            "selected_platforms": [],
            "confidence": "LOW",
            "reasoning": "Failed to parse routing decision",
            "clarification_needed": True,
            "content_focus": "Unknown"
        }


def build_clarification_message() -> str:
    """
    Build standardized clarification message for ambiguous requests.
    
    Returns:
        Formatted clarification message
    """
    return """I need more information to create the best content for you. Please specify:

1. **Content Topic**: What specific subject should the content cover?
2. **Target Platform(s)**: Which platform(s) do you want content for?
   - X/Twitter (quick, engaging posts)
   - LinkedIn (professional content) 
   - Instagram (visual storytelling)
   - Blog (comprehensive articles)
3. **Content Purpose**: What's your goal? (engagement, thought leadership, education, etc.)

Please provide these details so I can create targeted, high-quality content that fits your needs."""


def get_selected_content_agents(selected_platforms: List[str]) -> List[LlmAgent]:
    """
    Build list of content agents based on selected platforms.
    
    Args:
        selected_platforms: List of platform names
        
    Returns:
        List of corresponding content agents
    """
    from src.agents.content import (
        x_content_specialist,
        linkedin_content_specialist,
        instagram_content_specialist,
        blog_content_specialist
    )
    
    platform_agents = {
        "x_twitter": x_content_specialist,
        "linkedin": linkedin_content_specialist,
        "instagram": instagram_content_specialist,
        "blog": blog_content_specialist
    }
    
    agents = []
    for platform in selected_platforms:
        if platform in platform_agents:
            agents.append(platform_agents[platform])
        else:
            print(f"Warning: Unknown platform: {platform}")
    
    return agents