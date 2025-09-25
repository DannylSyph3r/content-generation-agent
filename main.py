"""
Smart Routing Social Media Content Pipeline
Interactive showcase demonstrating intelligent platform selection

SMART ROUTING FEATURES:
- Conditional platform execution based on request analysis
- Intelligent clarification handling for ambiguous requests
- Rate-limited multi-platform content generation
- Research-enhanced content with platform optimization

Usage: python main.py
"""
import asyncio
import time
from src.config.environment import check_environment
from src.config import RATE_LIMIT_DELAYS
from src.pipelines.smart_routing import create_smart_routed_content


async def interactive_smart_routing():
    """Interactive interface for smart routing social media pipeline."""
    
    print("\n>> Smart Routing Social Media Pipeline - Interactive Showcase")
    print("   Intelligent platform selection with conditional execution")
    print("=" * 70)
    print()
    print("SMART ROUTING FEATURES:")
    print("   1. INTELLIGENT SELECTION - Analyzes requests and selects optimal platforms")
    print("   2. CLARIFICATION HANDLING - Requests more info for ambiguous requests") 
    print("   3. CONDITIONAL EXECUTION - Only generates content for selected platforms")
    print("   4. RESEARCH ENHANCED - Incorporates current information and trends")
    print("   5. QUALITY OPTIMIZED - Reflection and refinement for better results")
    print()
    print("PLATFORM OPTIONS:")
    print("   - X/Twitter - Quick, engaging posts (280 chars)")
    print("   - LinkedIn - Professional thought leadership (500 words)")
    print("   - Instagram - Authentic storytelling (350 words)")
    print("   - Blog - Comprehensive articles (800-1500 words)")
    print()
    print("Type your content requests. Type 'quit' to exit.")
    print("=" * 70)
    print()
    print("Example requests:")
    print("   1. Create LinkedIn content about AI trends")
    print("   2. Write an Instagram post about productivity tips")
    print("   3. Generate X content about sustainable technology")
    print("   4. Create blog content about remote work productivity")
    print("   5. Make content for LinkedIn and Instagram about leadership")
    print()
    print("=" * 70)
    
    while True:
        print(f"\nEnter your request (or 'quit'): ", end="")
        user_request = input().strip()
        
        if user_request.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using Smart Routing Pipeline!")
            print("Smart routing makes content creation more efficient and targeted.")
            break
        
        if not user_request:
            print("Please enter a request or type 'quit' to exit.")
            continue
        
        print("\n" + "-" * 60)
        print("Processing your request...")
        print("This may take 30-60 seconds due to multi-agent processing")
        print("-" * 60)
        
        start_time = time.time()
        
        try:
            result = await create_smart_routed_content(user_request)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            print("\n" + "=" * 70)
            print("GENERATED CONTENT")
            print("=" * 70)
            print(result)
            print("=" * 70)
            print(f"\nExecution Time: {execution_time:.1f} seconds")
            print("Content successfully generated and optimized!")
            
        except Exception as e:
            print(f"\nError processing request: {e}")
            print("Please try again with a different request.")
        
        cooling_period = RATE_LIMIT_DELAYS["cooling_period"]
        print(f"\nCooling down for API rate limits ({cooling_period} seconds)...")
        await asyncio.sleep(cooling_period)
        print("Ready for next request!")


async def main():
    """Main execution function for smart routing pipeline."""
    
    print("\nEnvironment Check - Smart Routing Pipeline")
    print("-" * 50)
    
    # Check environment setup
    if not check_environment():
        print("Environment check failed. Please configure your API keys.")
        return
    
    print("Smart routing pipeline ready")
    print("-" * 50)
    print()
    
    # Start interactive interface
    await interactive_smart_routing()


if __name__ == "__main__":
    # Handle nested event loop for interactive environments
    try:
        import nest_asyncio
        nest_asyncio.apply()
    except ImportError:
        print("Note: nest_asyncio not available - running without nested loop support")
    
    # Run the main function
    asyncio.run(main())