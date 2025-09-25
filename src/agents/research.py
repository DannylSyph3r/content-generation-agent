"""
Research Enhancement Agent
Provides current information and trends for content enhancement
"""
from google.adk.agents import LlmAgent
from src.config.settings import GEMINI_TEXT_MODEL

# Try to import google_search tool
try:
    from google.adk.tools import google_search
    GOOGLE_SEARCH_AVAILABLE = True
    research_tools = [google_search]
except ImportError:
    GOOGLE_SEARCH_AVAILABLE = False
    research_tools = []
    print("Note: Google Search tool not available - using simulated research")


research_agent = LlmAgent(
    name="ResearchEnhancer",
    model=GEMINI_TEXT_MODEL,
    description="Research agent that gathers current information for content enhancement.",
    instruction="""You are a research specialist. Gather current, relevant information to enhance content creation.

RESEARCH OBJECTIVES:
1. Find current trends and data related to the topic
2. Identify key statistics and facts
3. Discover unique angles or perspectives
4. Gather supporting evidence and examples
5. Find relevant expert opinions or case studies

OUTPUT FORMAT:
**RESEARCH INSIGHTS**

**Current Trends**:
- [2-3 relevant current trends]

**Key Data Points**:
- [2-3 important statistics or facts]

**Unique Angles**:
- [1-2 interesting perspectives]

**Supporting Evidence**:
- [1-2 examples or case studies]

**Content Enhancement Value**:
[How this research improves the content]

Keep research concise and directly applicable to content creation.
Focus on information that adds credibility and engagement value.""",
    tools=research_tools,
    output_key="research_insights"
)