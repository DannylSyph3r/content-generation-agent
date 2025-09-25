"""
Simple Demo Scripts for Smart Routing Social Media Content Pipeline
Basic demonstrations of pipeline functionality with clear explanations
"""
import asyncio
from src.pipelines.smart_routing import create_smart_routed_content
from src.config.environment import check_environment


async def simple_demo():
    """Run a simple demonstration of the smart routing pipeline."""
    print("\n=== SIMPLE SMART ROUTING DEMO ===")
    print("Demonstrating intelligent platform selection with research enhancement")
    print("-" * 50)
    
    request = "Create content about the latest trends in sustainable technology and renewable energy"
    
    print(f"Request: {request}")
    print("Pipeline will automatically:")
    print("   • Analyze the request")
    print("   • Select optimal platforms")
    print("   • Research current trends") 
    print("   • Generate platform-optimized content")
    print("   • Apply quality feedback")
    print()
    print("Processing... (may take 30-60 seconds)")
    print("-" * 50)
    
    result = await create_smart_routed_content(request)
    
    print("\n--- GENERATED CONTENT ---")
    print("=" * 50)
    print(result)
    print("=" * 50)
    print("Simple demo completed successfully!")
    print("Notice how the pipeline automatically selected appropriate platforms")


async def platform_specific_demo():
    """Demonstrate platform-specific content generation."""
    print("\n=== PLATFORM-SPECIFIC ROUTING DEMO ===")
    print("Testing smart routing with platform-specific requests")
    print("-" * 50)
    
    demos = [
        {
            "request": "Create LinkedIn content about AI transforming healthcare",
            "platform": "LinkedIn",
            "expected": "Professional, business-focused content"
        },
        {
            "request": "Write an Instagram post about morning productivity tips",
            "platform": "Instagram", 
            "expected": "Visual, authentic, story-driven content"
        },
        {
            "request": "Generate a tweet about climate change innovations",
            "platform": "X/Twitter",
            "expected": "Concise, engaging, hashtag-optimized"
        },
        {
            "request": "Create a blog post about remote work best practices", 
            "platform": "Blog",
            "expected": "Comprehensive, SEO-optimized, detailed"
        }
    ]
    
    for i, demo in enumerate(demos, 1):
        print(f"\n>> DEMO {i}/4: {demo['platform']} Content")
        print(f"   Request: {demo['request']}")
        print(f"   Expected: {demo['expected']}")
        print("-" * 40)
        
        try:
            result = await create_smart_routed_content(demo['request'])
            
            # Show first 300 chars for brevity in multi-demo
            preview = result[:300] + "..." if len(result) > 300 else result
            print("   Generated Content Preview:")
            print(f"   {preview}")
            
            print(f"   Successfully generated {demo['platform']} content")
            
        except Exception as e:
            print(f"   Error: {e}")
        
        # Rate limiting between demos
        if i < len(demos):
            print("   Cooling down for API rate limits (15 seconds)...")
            await asyncio.sleep(15)
    
    print(f"\nPlatform-specific routing demo completed!")
    print("Each platform received content optimized for its specific requirements")


async def multi_platform_demo():
    """Demonstrate multi-platform content generation."""
    print("\n=== MULTI-PLATFORM ROUTING DEMO ===")
    print("Testing intelligent routing with multi-platform requests")
    print("-" * 50)
    
    request = "Create content for LinkedIn and Instagram about the importance of work-life balance for entrepreneurs in 2025"
    
    print(f"Request: {request}")
    print("Pipeline will:")
    print("   • Recognize both LinkedIn and Instagram are specified")
    print("   • Route to both platform specialists")
    print("   • Generate platform-optimized content for each")
    print("   • Apply research enhancement")
    print("   • Provide quality assessment")
    print()
    print("Processing multi-platform request... (may take 60-90 seconds)")
    print("-" * 40)
    
    try:
        result = await create_smart_routed_content(request)
        
        print("\n--- MULTI-PLATFORM CONTENT PACKAGE ---")
        print("=" * 50)
        print(result)
        print("=" * 50)
        print("Multi-platform routing demo completed!")
        print("Notice how each platform received tailored, optimized content")
        
    except Exception as e:
        print(f"Error generating multi-platform content: {e}")


async def research_enhancement_demo():
    """Demonstrate research enhancement capabilities."""
    print("\n=== RESEARCH ENHANCEMENT DEMO ===")
    print("Testing pipeline's ability to integrate current information")
    print("-" * 50)
    
    request = "Create content about the latest developments in electric vehicle technology this year"
    
    print(f"Request: {request}")
    print("This request specifically needs current information")
    print("Pipeline will:")
    print("   • Recognize need for current data")
    print("   • Perform research enhancement")
    print("   • Integrate findings into content")
    print("   • Generate informed, up-to-date content")
    print()
    print("Processing with research enhancement... (may take 45-75 seconds)")
    print("-" * 40)
    
    try:
        result = await create_smart_routed_content(request)
        
        print("\n--- RESEARCH-ENHANCED CONTENT ---")
        print("=" * 50)
        print(result)
        print("=" * 50)
        print("Research enhancement demo completed!")
        print("Content includes current information and trends from research")
        
    except Exception as e:
        print(f"Error with research-enhanced generation: {e}")


async def comprehensive_demo():
    """Run all demo scenarios in sequence."""
    print("\nCOMPREHENSIVE SMART ROUTING DEMONSTRATION")
    print("=" * 60)
    
    demos = [
        ("Simple Demo", simple_demo),
        ("Platform-Specific Demo", platform_specific_demo), 
        ("Multi-Platform Demo", multi_platform_demo),
        ("Research Enhancement Demo", research_enhancement_demo)
    ]
    
    for i, (name, demo_func) in enumerate(demos, 1):
        try:
            await demo_func()
            
            if i < len(demos):
                print(f"\nDemo {i}/{len(demos)} completed. Preparing next demo...")
                print("   (Adding cooldown period for API rate limits)")
                await asyncio.sleep(20)
                
        except Exception as e:
            print(f"Error in {name}: {e}")
    
    print("\n" + "=" * 60)
    print("ALL DEMOS COMPLETED SUCCESSFULLY!")
    print()
    print("KEY FEATURES DEMONSTRATED:")
    print("   - Intelligent platform selection and routing")
    print("   - Platform-specific content optimization")
    print("   - Multi-platform content generation")
    print("   - Research enhancement integration")
    print("   - Quality feedback and assessment")
    print("   - Conditional execution for efficiency")
    print()
    print("The Smart Routing Pipeline is ready for production use!")
    print("=" * 60)


if __name__ == "__main__":
    print("Smart Routing Social Media Content Pipeline - Demo Suite")
    print("   Showcasing intelligent platform selection with conditional execution")
    
    if not check_environment():
        print("Environment check failed. Please configure your API keys.")
        exit(1)
    
    print("Environment check passed!")
    
    # Ask user which demo to run
    print("\nSelect demo type:")
    print("1. Simple Demo (basic smart routing)")
    print("2. Platform-Specific Demo (routing optimization)")
    print("3. Multi-Platform Demo (intelligent multi-platform routing)")
    print("4. Research Enhancement Demo (current information integration)")
    print("5. Comprehensive Demo (all features)")
    
    choice = input("\nEnter your choice (1-5) or press Enter for Simple Demo: ").strip()
    
    async def run_selected_demo():
        if choice == "2":
            await platform_specific_demo()
        elif choice == "3":
            await multi_platform_demo()
        elif choice == "4":
            await research_enhancement_demo()
        elif choice == "5":
            await comprehensive_demo()
        else:
            # Default to simple demo
            await simple_demo()
    
    try:
        asyncio.run(run_selected_demo())
        print("\nThanks for trying the Smart Routing Pipeline demos!")
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user")
    except Exception as e:
        print(f"\nDemo error: {e}")
        print("Try running the environment check: python src/config/environment.py")