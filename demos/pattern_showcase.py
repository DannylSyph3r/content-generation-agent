"""
Agentic Patterns Demonstration
Interactive showcase of routing, parallelization, and reflection patterns
"""
import asyncio
import time
from typing import Dict, Any, List
from src.config.environment import check_environment
from src.pipelines.research_enhanced import create_content


class AgenticPatternsDemo:
    """Interactive demonstration of agentic design patterns."""
    
    def __init__(self):
        """Initialize demo with predefined scenarios."""
        self.demo_requests = [
            {
                "request": "Create LinkedIn content about the future of AI in business",
                "description": "Professional B2B content with thought leadership",
                "patterns_highlighted": ["routing", "parallelization", "reflection", "research"]
            },
            {
                "request": "Write Instagram and X content about productivity hacks for entrepreneurs",
                "description": "Multi-platform content with different tones",
                "patterns_highlighted": ["routing", "parallelization", "reflection"]
            },
            {
                "request": "Generate a comprehensive blog post about sustainable technology trends",
                "description": "Long-form content with deep analysis",
                "patterns_highlighted": ["routing", "research", "reflection"]
            }
        ]
    
    def print_header(self):
        """Print demo header and explanation."""
        print("\n" + "=" * 80)
        print("AGENTIC DESIGN PATTERNS - COMPREHENSIVE DEMONSTRATION")
        print("=" * 80)
        print()
        print("This demo showcases three core agentic design patterns:")
        print()
        print("1. ROUTING PATTERN")
        print("   - Smart request analysis and platform determination")
        print("   - Intelligent content strategy selection")
        print("   - Optimal platform matching")
        print()
        print("2. PARALLELIZATION PATTERN")
        print("   - Multiple specialized agents for different platforms")
        print("   - Concurrent content generation (sequential for free tier)")
        print("   - Platform-specific optimization")
        print()
        print("3. REFLECTION PATTERN")
        print("   - Quality assessment and evaluation")
        print("   - Iterative improvement and refinement")
        print("   - Continuous optimization feedback")
        print()
        print("RESEARCH ENHANCEMENT:")
        print("   - Real-time information gathering")
        print("   - Current trends and data integration")
        print("   - Enhanced content relevance and accuracy")
        print()
        print("=" * 80)
    
    def print_pattern_explanation(self, pattern: str):
        """Print detailed explanation of a specific pattern."""
        explanations = {
            "routing": """
ROUTING PATTERN IN ACTION:
   The SmartRouter agent analyzes your request to determine:
   - What type of content you need
   - Which platforms are optimal for your message
   - What content strategy will work best
   - Whether research enhancement is needed
   
   This intelligent routing ensures the right content goes to the right platforms
   with the right approach, maximizing engagement and effectiveness.
""",
            "parallelization": """
PARALLELIZATION PATTERN IN ACTION:
   Multiple specialized agents work on your content:
   - X/Twitter Specialist - Optimizes for 280-character engagement
   - LinkedIn Specialist - Creates professional thought leadership
   - Instagram Specialist - Develops authentic storytelling
   - Blog Specialist - Produces comprehensive informative content
   
   Each agent is an expert in their platform, ensuring optimal content
   for each audience and format (executed sequentially for free tier).
""",
            "reflection": """
REFLECTION PATTERN IN ACTION:  
   The QualityReflector and ContentRefiner agents:
   - Evaluate content quality across all platforms
   - Assess research integration effectiveness
   - Check for engagement potential and brand consistency
   - Identify specific improvement opportunities
   - Apply targeted refinements where needed
   
   This ensures high-quality, consistent content that meets
   professional standards and maximizes performance.
"""
        }
        print(explanations.get(pattern, ""))
    
    async def run_single_demo(self, demo_config: Dict[str, Any], demo_number: int):
        """Run a single demo with detailed pattern highlighting."""
        print(f"\n>> DEMO {demo_number}: {demo_config['description']}")
        print(f"   Request: \"{demo_config['request']}\"")
        print(f"   Patterns Highlighted: {', '.join(demo_config['patterns_highlighted'])}")
        print("-" * 60)
        
        # Explain patterns being demonstrated
        for pattern in demo_config['patterns_highlighted']:
            if pattern != 'research':  # Research is enhancement, not core pattern
                self.print_pattern_explanation(pattern)
        
        print(">> EXECUTING PIPELINE...")
        print("   This showcases all patterns in action - please wait...")
        print()
        
        start_time = time.time()
        
        try:
            result = await create_content(demo_config['request'])
            end_time = time.time()
            
            print(">> DEMO COMPLETED SUCCESSFULLY!")
            print(f"   Execution Time: {end_time - start_time:.1f} seconds")
            print()
            print("--- GENERATED CONTENT ---")
            print("=" * 60)
            print(result)
            print("=" * 60)
            
            # Highlight what patterns were demonstrated
            print("\nPATTERN DEMONSTRATION RESULTS:")
            if "routing" in demo_config['patterns_highlighted']:
                print("   - ROUTING: Request analyzed and optimal platform strategy determined")
            if "parallelization" in demo_config['patterns_highlighted']:
                print("   - PARALLELIZATION: Multiple specialized agents created platform-specific content")
            if "reflection" in demo_config['patterns_highlighted']:
                print("   - REFLECTION: Quality assessed and improvements applied")
            if "research" in demo_config['patterns_highlighted']:
                print("   - RESEARCH: Current information integrated for relevance")
            
        except Exception as e:
            print(f"Error: Demo failed - {e}")
            return False
        
        return True
    
    async def run_comprehensive_demo(self):
        """Run comprehensive demo of all patterns."""
        if not check_environment():
            print("Environment check failed. Please configure your API keys.")
            return
        
        self.print_header()
        
        print(">> STARTING COMPREHENSIVE AGENTIC PATTERNS DEMONSTRATION")
        print()
        
        successful_demos = 0
        
        for i, demo_config in enumerate(self.demo_requests, 1):
            success = await self.run_single_demo(demo_config, i)
            if success:
                successful_demos += 1
            
            # Add delay between demos for free tier
            if i < len(self.demo_requests):
                print("\nAdding delay for API rate limiting...")
                await asyncio.sleep(20)  # Longer delay between demos
        
        print("\n" + "=" * 80)
        print("COMPREHENSIVE DEMO COMPLETED!")
        print(f"Successful Demos: {successful_demos}/{len(self.demo_requests)}")
        print()
        print("AGENTIC DESIGN PATTERNS DEMONSTRATED:")
        print("   - ROUTING - Smart request analysis and platform selection")
        print("   - PARALLELIZATION - Multiple specialized content agents")
        print("   - REFLECTION - Quality assessment and iterative improvement")
        print()
        print("RESEARCH ENHANCEMENT SHOWCASED:")
        print("   - Real-time information gathering for current, relevant content")
        print()
        print("KEY BENEFITS DEMONSTRATED:")
        print("   - Intelligent content strategy through routing")
        print("   - Platform-optimized content through specialization")  
        print("   - High-quality output through reflection and refinement")
        print("   - Current and relevant content through research integration")
        print()
        print("READY FOR PRODUCTION USE!")
        print("=" * 80)


if __name__ == "__main__":
    demo = AgenticPatternsDemo()
    asyncio.run(demo.run_comprehensive_demo())