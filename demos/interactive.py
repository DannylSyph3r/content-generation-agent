"""
Interactive CLI Demo for Smart Routing Pipeline
Allows users to explore specific features interactively
"""
import asyncio
from src.config.environment import check_environment
from src.pipelines.smart_routing import create_smart_routed_content
from demos.pattern_showcase import AgenticPatternsDemo


async def interactive_cli():
    """Interactive command-line interface for exploring the pipeline."""
    
    if not check_environment():
        print("Environment check failed. Please configure your API keys.")
        return
    
    print("\n" + "=" * 70)
    print("SMART ROUTING PIPELINE - INTERACTIVE CLI")
    print("=" * 70)
    print()
    print("Welcome to the interactive demonstration interface!")
    print("Explore different features and patterns of the pipeline.")
    print()
    
    while True:
        print("\n" + "-" * 50)
        print("MAIN MENU")
        print("-" * 50)
        print("1. Quick Content Generation")
        print("2. Platform-Specific Demo")
        print("3. Multi-Platform Demo")
        print("4. Agentic Patterns Showcase")
        print("5. Custom Request")
        print("6. Exit")
        print()
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            await quick_generation()
        elif choice == "2":
            await platform_specific_menu()
        elif choice == "3":
            await multi_platform_generation()
        elif choice == "4":
            await patterns_showcase_menu()
        elif choice == "5":
            await custom_request()
        elif choice == "6":
            print("\nThank you for using Smart Routing Pipeline!")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


async def quick_generation():
    """Quick content generation with predefined topics."""
    print("\n>> QUICK CONTENT GENERATION")
    print("Select a topic:")
    print("1. AI and Technology")
    print("2. Productivity and Work")
    print("3. Sustainability")
    print("4. Leadership")
    print("5. Back to Main Menu")
    
    topic_choice = input("\nSelect topic (1-5): ").strip()
    
    topics = {
        "1": "Create content about the latest AI trends and their business impact",
        "2": "Write about productivity tips for remote workers",
        "3": "Generate content about sustainable business practices",
        "4": "Create content about effective leadership in 2025"
    }
    
    if topic_choice in topics:
        request = topics[topic_choice]
        print(f"\nGenerating content for: {request}")
        print("Please wait...")
        
        result = await create_smart_routed_content(request)
        print("\n--- GENERATED CONTENT ---")
        print(result)
        print("-" * 50)
    elif topic_choice != "5":
        print("Invalid option.")


async def platform_specific_menu():
    """Platform-specific content generation menu."""
    print("\n>> PLATFORM-SPECIFIC GENERATION")
    print("Select a platform:")
    print("1. LinkedIn")
    print("2. X/Twitter")
    print("3. Instagram")
    print("4. Blog")
    print("5. Back to Main Menu")
    
    platform_choice = input("\nSelect platform (1-5): ").strip()
    
    platforms = {
        "1": "LinkedIn",
        "2": "X",
        "3": "Instagram",
        "4": "blog"
    }
    
    if platform_choice in platforms:
        platform = platforms[platform_choice]
        topic = input(f"Enter topic for {platform} content: ").strip()
        
        if topic:
            request = f"Create {platform} content about {topic}"
            print(f"\nGenerating {platform} content...")
            print("Please wait...")
            
            result = await create_smart_routed_content(request)
            print("\n--- GENERATED CONTENT ---")
            print(result)
            print("-" * 50)
    elif platform_choice != "5":
        print("Invalid option.")


async def multi_platform_generation():
    """Generate content for multiple platforms."""
    print("\n>> MULTI-PLATFORM GENERATION")
    print("Select platforms (comma-separated):")
    print("Options: linkedin, x, instagram, blog")
    
    platforms = input("Enter platforms: ").strip().lower()
    topic = input("Enter topic: ").strip()
    
    if platforms and topic:
        request = f"Create content for {platforms} about {topic}"
        print(f"\nGenerating multi-platform content...")
        print("Please wait...")
        
        result = await create_smart_routed_content(request)
        print("\n--- GENERATED CONTENT ---")
        print(result)
        print("-" * 50)


async def patterns_showcase_menu():
    """Showcase specific agentic patterns."""
    print("\n>> AGENTIC PATTERNS SHOWCASE")
    print("1. Routing Pattern Demo")
    print("2. Parallelization Pattern Demo")
    print("3. Reflection Pattern Demo")
    print("4. Full Patterns Demo")
    print("5. Back to Main Menu")
    
    pattern_choice = input("\nSelect option (1-5): ").strip()
    
    if pattern_choice == "4":
        demo = AgenticPatternsDemo()
        await demo.run_comprehensive_demo()
    elif pattern_choice in ["1", "2", "3"]:
        pattern_names = {
            "1": "routing",
            "2": "parallelization",
            "3": "reflection"
        }
        pattern = pattern_names[pattern_choice]
        
        demo = AgenticPatternsDemo()
        demo.print_pattern_explanation(pattern)
        
        print(f"\nRunning {pattern} pattern demo...")
        # Create a demo request highlighting this pattern
        request = f"Create content demonstrating the {pattern} pattern"
        result = await create_smart_routed_content(request)
        
        print("\n--- PATTERN DEMO RESULT ---")
        print(result)
        print("-" * 50)
    elif pattern_choice != "5":
        print("Invalid option.")


async def custom_request():
    """Process a custom user request."""
    print("\n>> CUSTOM REQUEST")
    print("Enter your content request (or 'back' to return):")
    
    request = input("\nYour request: ").strip()
    
    if request.lower() != 'back' and request:
        print("\nProcessing your custom request...")
        print("Please wait...")
        
        result = await create_smart_routed_content(request)
        print("\n--- GENERATED CONTENT ---")
        print(result)
        print("-" * 50)


if __name__ == "__main__":
    asyncio.run(interactive_cli())