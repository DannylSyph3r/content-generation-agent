"""
Environment validation for Social Media Content Pipeline
Checks all required dependencies and configurations.
"""
import os
import sys
from dotenv import load_dotenv


def check_environment() -> bool:
    """
    Check if the environment is properly configured for the social media pipeline.
    
    Returns:
        bool: True if environment is properly configured, False otherwise
    """
    # Load environment variables
    load_dotenv()
    
    # Test required ADK imports
    try:
        from google.adk.agents import LlmAgent
        from google.adk.runners import InMemoryRunner
        from google.genai import types
        print(">> Google ADK imported successfully")
    except ImportError as e:
        print(f"Error: Failed to import required ADK modules: {e}")
        print("      Run: pip install google-adk")
        return False
    
    # Check API key
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables")
        print("      Please set GOOGLE_API_KEY in your .env file")
        return False
    
    print(">> GOOGLE_API_KEY configured")
    
    # Show model configuration
    gemini_model = os.getenv("GEMINI_TEXT_MODEL", "gemini-2.5-flash")
    print(f">> GEMINI_TEXT_MODEL: {gemini_model}")
    
    return True


def print_environment_info():
    """Print detailed environment information for debugging."""
    print("\nEnvironment Details:")
    print("-" * 40)
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    
    # Check if .env file exists
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"Environment file found: {env_file}")
    else:
        print(f"Warning: Environment file not found: {env_file}")
    
    # List Google/Gemini environment variables
    sensitive_keys = ['API_KEY', 'SECRET', 'TOKEN']
    env_vars = []
    for key, value in os.environ.items():
        if key.startswith(('GOOGLE_', 'GEMINI_')):
            if any(sensitive in key.upper() for sensitive in sensitive_keys):
                env_vars.append(f"{key}=***hidden***")
            else:
                env_vars.append(f"{key}={value}")
    
    if env_vars:
        print("Environment variables:")
        for var in sorted(env_vars):
            print(f"  {var}")
    
    print("-" * 40)


if __name__ == "__main__":
    print("Environment Check - Social Media Content Pipeline")
    print("-" * 50)
    
    if check_environment():
        print("\nEnvironment validation successful!")
        print_environment_info()
    else:
        print("\nEnvironment validation failed!")
        print("\nPlease ensure:")
        print("1. Google ADK is installed: pip install google-adk")
        print("2. GOOGLE_API_KEY is set in .env file")
        sys.exit(1)