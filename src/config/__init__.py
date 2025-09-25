"""
Configuration package for Smart Routing Social Media Content Pipeline
Complete configuration supporting intelligent platform selection.
"""

from .settings import (
    GOOGLE_API_KEY,
    GEMINI_TEXT_MODEL,
    SOCIAL_MEDIA_CONFIGS,
    BRAND_GUIDELINES,
    QUALITY_THRESHOLDS,
    SUPPORTED_PLATFORMS,
    RATE_LIMIT_DELAY,
    MAX_RETRIES,
    get_platform_config,
    get_all_platform_names,
    validate_platform
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
        "iterations": 1,  # Number of reflection cycles
        "description": "Quality assessment and iterative improvement"
    }
}

# Research enhancement configuration
RESEARCH_CONFIG = {
    "enabled": True,
    "search_queries_per_topic": 2,
    "max_sources": 3,
    "fallback_mode": "strategic_analysis"  # When Google Search not available
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
    },
    "rate_limiting": {
        "delay_between_platforms": 7,  # seconds
        "cooling_period": 15  # seconds between user requests
    }
}

__all__ = [
    'GOOGLE_API_KEY',
    'GEMINI_TEXT_MODEL',
    'SOCIAL_MEDIA_CONFIGS',
    'BRAND_GUIDELINES', 
    'QUALITY_THRESHOLDS',
    'SUPPORTED_PLATFORMS',
    'RATE_LIMIT_DELAY',
    'MAX_RETRIES',
    'APP_NAME',
    'USER_ID',
    'SESSION_ID',
    'AGENTIC_PATTERNS',
    'RESEARCH_CONFIG',
    'ROUTING_CONFIG',
    'get_platform_config',
    'get_all_platform_names',
    'validate_platform',
    'check_environment'
]

__version__ = "5.0.0"  # Smart routing version