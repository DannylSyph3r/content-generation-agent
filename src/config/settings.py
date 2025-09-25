"""
Configuration settings for Smart Routing Social Media Content Pipeline
Cleaned up to include only actively used settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_TEXT_MODEL = os.getenv("GEMINI_TEXT_MODEL", "gemini-2.5-flash")

# Quality Control Settings
QUALITY_SCORE_THRESHOLD = 6.5
MAX_QUALITY_ATTEMPTS = 3

# Rate Limiting Configuration
RATE_LIMIT_DELAYS = {
    "after_routing": 4,        # Seconds after routing decision
    "after_research": 2,       # Seconds after research
    "between_platforms": 3,    # Seconds between platform content generation  
    "cooling_period": 15       # Seconds between user requests
}

# Supported Platforms
SUPPORTED_PLATFORMS = ["x_twitter", "linkedin", "instagram", "blog"]