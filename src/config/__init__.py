"""
Configuration package for Smart Routing Social Media Content Pipeline
Exports actively used settings and constants.
"""

from .settings import (
    GOOGLE_API_KEY,
    GEMINI_TEXT_MODEL,
    QUALITY_SCORE_THRESHOLD,
    MAX_QUALITY_ATTEMPTS,
    RATE_LIMIT_DELAYS,
    SUPPORTED_PLATFORMS
)

from .environment import check_environment

# Application constants for ADK
APP_NAME = "smart_routing_social_media_generator"
USER_ID = "demo_user"
SESSION_ID = "demo_session"

# Smart routing design pattern configuration
AGENTIC_PATTERNS = {
    "smart_routing": {
        "enabled": True,
        "description": "Intelligent platform selection with conditional execution",
        "confidence_threshold": "HIGH"
    },
    "conditional_execution": {
        "enabled": True,
        "mode": "sequential",  # "sequential" for free tier, "parallel" for paid
        "description": "Platform-specific content generation based on routing decisions"
    },
    "reflection": {
        "enabled": True,
        "iterations": 1,
        "description": "Quality assessment and iterative improvement"
    }
}

# Research enhancement configuration
RESEARCH_CONFIG = {
    "enabled": True,
    "search_queries_per_topic": 2,
    "max_sources": 3,
    "fallback_mode": "strategic_analysis"
}

# Smart routing specific configurations
ROUTING_CONFIG = {
    "platform_selection": {
        "max_platforms": 3,
        "confidence_levels": ["HIGH", "MEDIUM", "LOW"],
        "clarification_threshold": "LOW"
    },
    "clarification_handling": {
        "enabled": True,
        "end_conversation": True,
        "message_template": "clarification_request"
    }
}

__all__ = [
    'GOOGLE_API_KEY',
    'GEMINI_TEXT_MODEL',
    'QUALITY_SCORE_THRESHOLD',
    'MAX_QUALITY_ATTEMPTS',
    'RATE_LIMIT_DELAYS',
    'SUPPORTED_PLATFORMS',
    'APP_NAME',
    'USER_ID',
    'SESSION_ID',
    'AGENTIC_PATTERNS',
    'RESEARCH_CONFIG',
    'ROUTING_CONFIG',
    'check_environment'
]

__version__ = "5.0.0"