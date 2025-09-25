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
    
    # Check Python version
    if sys.version_info < (3, 8):
        print(f"Error: Python {sys.version_info.major}.{sys.version_info.minor} - requires Python 3.8+")
        return False
    
    # Test ADK imports
    try:
        import google.adk
        from google.adk.agents import LlmAgent, SequentialAgent
        from google.adk.runners import InMemoryRunner
        from google.genai import types
        print(">> Google ADK imported successfully")
    except ImportError as e:
        print(f"Error: Failed to import required ADK modules: {e}")
        return False
    
    # Check environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables")
        print("      Please set GOOGLE_API_KEY in your .env file or environment")
        return False
    
    print(">> GOOGLE_API_KEY configured")
    
    # Check Gemini model configuration
    gemini_model = os.getenv("GEMINI_TEXT_MODEL", "gemini-2.5-flash")
    print(f">> GEMINI_TEXT_MODEL: {gemini_model}")
    
    # Test Google Search availability (optional)
    try:
        from google.adk.tools import google_search
        print(">> Google Search tool available")
    except ImportError:
        print("Note: Google Search tool not available - will use simulated research")
    
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
    
    # List available environment variables (without exposing sensitive data)
    sensitive_keys = ['GOOGLE_API_KEY', 'API_KEY', 'SECRET', 'TOKEN']
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
        print("1. Python 3.8+ is installed")
        print("2. Google ADK is installed: pip install google-adk")
        print("3. GOOGLE_API_KEY is set in .env file or environment")
        print("4. All required dependencies are installed")
        sys.exit(1)