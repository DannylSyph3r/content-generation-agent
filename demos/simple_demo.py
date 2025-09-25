"""
Simple Demo Scripts for Social Media Content Pipeline
Basic demonstrations of pipeline functionality
"""
import asyncio
from src.pipelines.smart_routing import create_smart_routed_content
from src.config.environment import check_environment


async def simple_demo():
    """Run a simple demonstration of the pipeline."""
    print("\n=== SIMPLE DEMO ===")
    print("Creating content about sustainable technology")
    print("-" * 50)
    
    request = "Create content about the latest trends in sustainable technology and renewable energy"
    result = await create_smart_routed_content(request)
    
    print("\n--- GENERATED CONTENT ---")
    print(result)
    print("-" * 50)
    print("Simple demo completed!")


async def platform_specific_demo():
    """Demonstrate platform-specific content generation."""
    print("\n=== PLATFORM-SPECIFIC DEMO ===")
    print("Generating targeted content for specific platforms")
    print("-" * 50)
    
    demos = [
        ("Create LinkedIn content about AI in healthcare", "LinkedIn"),
        ("Write an Instagram post about morning productivity tips", "Instagram"),
        ("Generate a tweet about climate change innovations", "X/Twitter"),
        ("Create a blog post about remote work best practices", "Blog")
    ]
    
    for request, platform in demos:
        print(f"\n>> Generating {platform} content...")
        print(f"   Request: {request}")
        print("-" * 40)
        
        result = await create_smart_routed_content(request)
        
        # Show only first 500 chars for brevity
        preview = result[:500] + "..." if len(result) > 500 else result
        print(preview)
        
        # Rate limiting
        print("\n   Cooling down for API rate limits...")
        await asyncio.sleep(15)
    
    print("\nPlatform-specific demo completed!")


async def multi_platform_demo():
    """Demonstrate multi-platform content generation."""
    print("\n=== MULTI-PLATFORM DEMO ===")
    print("Creating content for multiple platforms simultaneously")
    print("-" * 50)
    
    request = "Create content for LinkedIn and Instagram about the importance of work-life balance in 2025"
    
    print(f"\nRequest: {request}")
    print("Expected: Content for both LinkedIn and Instagram")
    print("-" * 40)
    
    result = await create_smart_routed_content(request)
    
    print("\n--- MULTI-PLATFORM CONTENT ---")
    print(result)
    print("-" * 50)
    print("Multi-platform demo completed!")


async def comprehensive_demo():
    """Run all demo scenarios."""
    print("\n>> Comprehensive Social Media Content Generation Demo")
    print("=" * 60)
    
    # Run basic demo
    await simple_demo()
    
    # Wait for user input
    input("\nPress Enter to continue to platform-specific demo...")
    
    # Run platform-specific demo
    await platform_specific_demo()
    
    # Wait for user input
    input("\nPress Enter to continue to multi-platform demo...")
    
    # Run multi-platform demo
    await multi_platform_demo()
    
    print("\nAll demos completed successfully!")
    print("\nKey Features Demonstrated:")
    print("  - Single platform content generation")
    print("  - Multi-platform parallel processing") 
    print("  - Platform-specific optimizations")
    print("  - Quality assurance and validation")
    print("  - Professional, publication-ready output")


if __name__ == "__main__":
    print("Starting Social Media Content Generation Demo")
    
    if not check_environment():
        print("Environment check failed. Please configure your API keys.")
        exit(1)
    
    # Ask user which demo to run
    print("\nSelect demo type:")
    print("1. Simple Demo (basic functionality)")
    print("2. Platform-Specific Demo (optimization focus)")
    print("3. Multi-Platform Demo (parallel processing)")
    print("4. Comprehensive Demo (all features)")
    
    choice = input("\nEnter your choice (1-4) or press Enter for Simple Demo: ").strip()
    
    if choice == "2":
        asyncio.run(platform_specific_demo())
    elif choice == "3":
        asyncio.run(multi_platform_demo())
    elif choice == "4":
        asyncio.run(comprehensive_demo())
    else:
        # Default to simple demo
        asyncio.run(simple_demo())