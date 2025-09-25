"""
Complete Configuration settings for Research-Enhanced Social Media Pipeline
Supports all three agentic design patterns with research enhancement.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration - Optimized for free tier
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_TEXT_MODEL = os.getenv("GEMINI_TEXT_MODEL", "gemini-2.5-flash")

# Social Media Platform Configurations
SOCIAL_MEDIA_CONFIGS = {
    "x": {
        "name": "X (Twitter)",
        "character_limit": 280,
        "word_limit": 50,
        "style": "conversational, punchy, engaging",
        "hashtag_limit": 2,
        "tone": "casual yet impactful",
        "audience": "general public, trending topics",
        "best_practices": [
            "Strong hook in first 10 words",
            "Include call-to-action",
            "Use trending hashtags",
            "Ask engaging questions"
        ]
    },
    "linkedin": {
        "name": "LinkedIn",
        "character_limit": 3000,
        "word_limit": 500,
        "style": "professional, thought leadership, business-focused",
        "hashtag_limit": 5,
        "tone": "authoritative and insightful",
        "audience": "business professionals, decision-makers",
        "best_practices": [
            "Start with industry insight",
            "Share strategic perspectives", 
            "Include business impact",
            "End with professional question",
            "Use industry-specific hashtags"
        ]
    },
    "instagram": {
        "name": "Instagram",
        "character_limit": 2200,
        "word_limit": 350,
        "style": "authentic, story-driven, visual-first",
        "hashtag_limit": 15,
        "tone": "relatable and authentic",
        "audience": "visual-first community, lifestyle-focused",
        "best_practices": [
            "Personal, relatable opening",
            "Story-driven narrative",
            "Emotional connection points",
            "Community-building questions",
            "Mix of niche and broad hashtags"
        ]
    },
    "blog": {
        "name": "Blog/Article",
        "character_limit": 10000,
        "word_limit": 1500,
        "style": "comprehensive, informative, SEO-optimized",
        "hashtag_limit": 0,
        "tone": "authoritative and educational",
        "audience": "information seekers, long-form readers",
        "best_practices": [
            "SEO-optimized headline",
            "Clear structure with headers",
            "Data and examples",
            "Actionable takeaways",
            "Natural keyword integration"
        ]
    }
}

# Brand Guidelines
BRAND_GUIDELINES = {
    "voice": "knowledgeable, approachable, innovative",
    "values": ["authenticity", "expertise", "community", "innovation"],
    "topics_to_avoid": ["controversial politics", "unverified claims"],
    "preferred_tone": "professional yet conversational",
    "engagement_style": "thought-provoking questions and insights"
}

# Quality Thresholds
QUALITY_THRESHOLDS = {
    "minimum_quality_score": 7,
    "platform_fit_weight": 0.3,
    "engagement_potential_weight": 0.25,
    "research_integration_weight": 0.2,
    "brand_consistency_weight": 0.15,
    "value_delivery_weight": 0.1
}

# Supported Platforms
SUPPORTED_PLATFORMS = ["x", "linkedin", "instagram", "blog"]

# Rate Limiting Configuration (for free tier)
RATE_LIMIT_DELAY = 4  # seconds between API calls
MAX_RETRIES = 3

# Helper Functions
def get_platform_config(platform: str) -> dict:
    """Get configuration for a specific platform."""
    return SOCIAL_MEDIA_CONFIGS.get(platform.lower(), {})

def get_all_platform_names() -> list:
    """Get list of all configured platform names."""
    return [config["name"] for config in SOCIAL_MEDIA_CONFIGS.values()]

def validate_platform(platform: str) -> bool:
    """Check if a platform is supported."""
    return platform.lower() in SUPPORTED_PLATFORMS