"""
Smart Routing Pipeline Demonstration
Interactive showcase of intelligent platform selection with conditional execution
"""
import asyncio
import time
from typing import Dict, Any, List
from src.config.environment import check_environment
from src.pipelines.smart_routing import create_smart_routed_content


class SmartRoutingDemo:
    """Interactive demonstration of smart routing pipeline."""
    
    def __init__(self):
        """Initialize demo with predefined scenarios."""
        self.demo_requests = [
            {
                "request": "Create LinkedIn content about the future of AI in business",
                "description": "Professional B2B content with thought leadership",
                "expected_platforms": ["LinkedIn"],
                "features_highlighted": ["intelligent_platform_selection", "research_enhancement", "quality_feedback"]
            },
            {
                "request": "Write Instagram and X content about productivity hacks for entrepreneurs", 
                "description": "Multi-platform content with different tones",
                "expected_platforms": ["Instagram", "X/Twitter"],
                "features_highlighted": ["multi_platform_routing", "conditional_execution", "platform_optimization"]
            },
            {
                "request": "Generate a comprehensive blog post about sustainable technology trends",
                "description": "Long-form content with deep analysis", 
                "expected_platforms": ["Blog"],
                "features_highlighted": ["smart_routing", "research_enhancement", "quality_assessment"]
            }
        ]
    
    def print_header(self):
        """Print demo header and explanation."""
        print("\n" + "=" * 80)
        print("SMART ROUTING PIPELINE - COMPREHENSIVE DEMONSTRATION")
        print("=" * 80)
        print()
        print("This demo showcases the Smart Routing Pipeline featuring:")
        print()
        print("INTELLIGENT PLATFORM SELECTION")
        print("   • Analyzes requests to determine optimal platforms")
        print("   • Conditional execution - only generates for selected platforms")
        print("   • Handles clarification requests for ambiguous inputs")
        print()
        print("SMART CONTENT GENERATION")
        print("   • Platform-specific specialists for optimized content")
        print("   • Sequential generation (optimized for free tier)")
        print("   • Research-enhanced content with current information")
        print()
        print("QUALITY FEEDBACK LOOP")
        print("   • Quality assessment and scoring")
        print("   • Iterative improvement with feedback")
        print("   • Continuous optimization until quality threshold met")
        print()
        print("RESEARCH INTEGRATION")
        print("   • Real-time information gathering")
        print("   • Current trends and data integration")
        print("   • Enhanced content relevance and accuracy")
        print()
        print("=" * 80)
    
    def print_feature_explanation(self, features: List[str]):
        """Print explanation of features being demonstrated."""
        feature_explanations = {
            "intelligent_platform_selection": """
INTELLIGENT PLATFORM SELECTION:
   The pipeline analyzes your request to automatically determine which platforms
   would be most effective for your content, rather than generating for all platforms.""",
            
            "multi_platform_routing": """
MULTI-PLATFORM ROUTING:
   When multiple platforms are specified or implied, the system routes content
   creation to multiple specialists simultaneously (sequential execution for free tier).""",
            
            "conditional_execution": """
CONDITIONAL EXECUTION:
   Only generates content for platforms the routing agent determines are optimal.
   This saves API calls and focuses effort where it will be most effective.""",
            
            "research_enhancement": """
RESEARCH ENHANCEMENT:
   Integrates current information and trends to make content more relevant,
   accurate, and valuable to your audience.""",
            
            "quality_feedback": """
QUALITY FEEDBACK LOOP:
   Evaluates generated content quality and iteratively improves it based on
   specific feedback until it meets publication standards.""",
            
            "platform_optimization": """
PLATFORM OPTIMIZATION:
   Each platform has specialized agents that understand the unique requirements,
   audience expectations, and best practices for that specific platform.""",
            
            "quality_assessment": """
QUALITY ASSESSMENT:
   Comprehensive evaluation of content across multiple dimensions including
   engagement potential, platform fit, and value delivery."""
        }
        
        print("\n>> FEATURES BEING DEMONSTRATED:")
        for feature in features:
            if feature in feature_explanations:
                print(feature_explanations[feature])
        print()
    
    async def run_single_demo(self, demo_config: Dict[str, Any], demo_number: int):
        """Run a single demo with detailed feature highlighting."""
        print(f"\n>> DEMO {demo_number}: {demo_config['description']}")
        print(f"   Request: \"{demo_config['request']}\"")
        print(f"   Expected Platforms: {', '.join(demo_config['expected_platforms'])}")
        print("-" * 60)
        
        # Explain features being demonstrated
        self.print_feature_explanation(demo_config['features_highlighted'])
        
        print(">> EXECUTING SMART ROUTING PIPELINE...")
        print("   This may take 30-90 seconds due to multi-agent processing")
        print()
        
        start_time = time.time()
        
        try:
            result = await create_smart_routed_content(demo_config['request'])
            end_time = time.time()
            
            print(">> DEMO COMPLETED SUCCESSFULLY!")
            print(f"   Execution Time: {end_time - start_time:.1f} seconds")
            print()
            print("--- GENERATED CONTENT ---")
            print("=" * 60)
            print(result)
            print("=" * 60)
            
            # Highlight what features were demonstrated
            print("\n>> PIPELINE FEATURES DEMONSTRATED:")
            print("   - Smart platform analysis and selection")
            print("   - Conditional execution for optimal platforms only")
            print("   - Research-enhanced content generation")
            print("   - Quality assessment and feedback integration")
            print("   - Platform-specific optimization")
            
        except Exception as e:
            print(f"Demo failed - {e}")
            print("   This may be due to API rate limits or configuration issues")
            return False
        
        return True
    
    async def run_comprehensive_demo(self):
        """Run comprehensive demo of smart routing features."""
        if not check_environment():
            print("Environment check failed. Please configure your API keys.")
            return
        
        self.print_header()
        
        print(">> STARTING COMPREHENSIVE SMART ROUTING DEMONSTRATION")
        print()
        
        successful_demos = 0
        
        for i, demo_config in enumerate(self.demo_requests, 1):
            success = await self.run_single_demo(demo_config, i)
            if success:
                successful_demos += 1
            
            # Add delay between demos for rate limiting
            if i < len(self.demo_requests):
                print(f"\n⏳ Cooling down for API rate limiting (20 seconds)...")
                await asyncio.sleep(20)
        
        print("\n" + "=" * 80)
        print("COMPREHENSIVE DEMO COMPLETED!")
        print(f"Successful Demos: {successful_demos}/{len(self.demo_requests)}")
        print()
        print("SMART ROUTING FEATURES DEMONSTRATED:")
        print("   - INTELLIGENT SELECTION - Smart request analysis and platform selection")
        print("   - CONDITIONAL EXECUTION - Platform-specific content generation")
        print("   - QUALITY FEEDBACK - Assessment and iterative improvement")
        print("   - RESEARCH ENHANCED - Current information integration")
        print()
        print("KEY BENEFITS DEMONSTRATED:")
        print("   • More efficient API usage through smart routing")
        print("   • Platform-optimized content through specialization")  
        print("   • Higher quality output through feedback loops")
        print("   • Current and relevant content through research integration")
        print("   • Intelligent clarification handling for ambiguous requests")
        print()
        print("READY FOR PRODUCTION USE!")
        print("=" * 80)


if __name__ == "__main__":
    demo = SmartRoutingDemo()
    
    print("Starting Smart Routing Pipeline Demonstration")
    print("   This demo showcases intelligent platform selection with conditional execution")
    
    # Check environment first
    if not check_environment():
        print("Environment check failed. Please configure your API keys.")
        exit(1)
    
    # Ask user which demo to run
    print("\nSelect demo type:")
    print("1. Demo 1 - LinkedIn AI Business Content (Single Platform)")
    print("2. Demo 2 - Instagram + X Productivity Content (Multi-Platform)")
    print("3. Demo 3 - Blog Sustainable Tech Content (Long-Form)")
    print("4. Comprehensive Demo (All Features)")
    
    choice = input("\nEnter your choice (1-4) or press Enter for Comprehensive Demo: ").strip()
    
    async def run_selected_demo():
        demo_instance = SmartRoutingDemo()
        
        if choice == "1":
            await demo_instance.run_single_demo(demo_instance.demo_requests[0], 1)
        elif choice == "2":
            await demo_instance.run_single_demo(demo_instance.demo_requests[1], 2)
        elif choice == "3":
            await demo_instance.run_single_demo(demo_instance.demo_requests[2], 3)
        else:
            # Default to comprehensive demo
            await demo_instance.run_comprehensive_demo()
    
    asyncio.run(run_selected_demo())