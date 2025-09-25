"""
Research-Enhanced Content Pipeline
Alternative pipeline showcasing routing, parallelization, and reflection patterns
"""
from google.adk.agents import LlmAgent, SequentialAgent
from src.config.settings import GEMINI_TEXT_MODEL

# Try to import google_search
try:
    from google.adk.tools import google_search
    GOOGLE_SEARCH_AVAILABLE = True
except ImportError:
    GOOGLE_SEARCH_AVAILABLE = False
    print("Note: Google Search tool not available - using simulated research")


# PATTERN 1: ROUTING
routing_agent = LlmAgent(
    name="SmartRouter",
    model=GEMINI_TEXT_MODEL,
    description="Intelligent routing agent that analyzes requests and determines optimal content strategy.",
    instruction="""You are an expert social media strategist and content router. Your role is to analyze incoming requests and create an intelligent routing strategy.

ANALYSIS FRAMEWORK:
1. **Request Understanding**: What type of content is being requested?
2. **Platform Identification**: Which platforms are mentioned or implied?
3. **Content Complexity**: Simple post, detailed analysis, or comprehensive content?
4. **Research Requirements**: Does this need current information or trends?
5. **Audience Considerations**: Professional, casual, or mixed audience?

PLATFORM CAPABILITIES:
- **X/Twitter**: Quick insights, trending topics, conversational (280 chars)
- **LinkedIn**: Professional analysis, thought leadership, business focus (500 words)
- **Instagram**: Visual storytelling, personal connection, lifestyle (350 words)  
- **Blog/Article**: Deep-dive analysis, comprehensive coverage (800-1500 words)

OUTPUT FORMAT:
**ROUTING ANALYSIS**

**Request Type**: [Brief description of what user wants]
**Recommended Platforms**: [List 1-3 optimal platforms]
**Content Strategy**: [Approach for each platform]  
**Research Needs**: [What current information would enhance this content]
**Complexity Level**: [Simple/Medium/Complex]
**Execution Plan**: [How to approach content creation]

**ROUTING DECISION**
Proceeding with [platforms] strategy focusing on [main approach].
Research enhancement: [Yes/No and what to research]

Keep your analysis concise but thorough. Focus on actionable routing decisions.""",
    output_key="routing_analysis"
)


# PATTERN 2: PARALLELIZATION - Platform Specialists
x_specialist = LlmAgent(
    name="XSpecialist",
    model=GEMINI_TEXT_MODEL,
    description="X/Twitter content optimization expert.",
    instruction="""You are an X (Twitter) specialist. Create viral-worthy content optimized for maximum engagement.

REQUIREMENTS:
- **Strict 280 character limit**
- **Hook in first 10 words**
- **1-2 strategic hashtags only**
- **Include call-to-action or question**

When research data is provided, extract the most tweet-worthy insight.

OUTPUT:
[Your optimized 280-character tweet]

Write ONLY the tweet, no explanations.""",
    output_key="x_content"
)

linkedin_specialist = LlmAgent(
    name="LinkedInSpecialist", 
    model=GEMINI_TEXT_MODEL,
    description="LinkedIn professional content expert.",
    instruction="""You are a LinkedIn specialist. Create thought leadership content for professionals.

STRUCTURE (500 words max):
1. **Hook** (2 lines that appear before "see more")
2. **Context** (Problem or opportunity)
3. **Insights** (3-4 key points with business impact)
4. **Application** (How to implement)
5. **Question** (Drive engagement)

Include 3-5 professional hashtags.

OUTPUT:
[Your complete LinkedIn post]

Write ONLY the post content.""",
    output_key="linkedin_content"
)

instagram_specialist = LlmAgent(
    name="InstagramSpecialist",
    model=GEMINI_TEXT_MODEL, 
    description="Instagram storytelling expert.",
    instruction="""You are an Instagram specialist. Create authentic, story-driven content.

REQUIREMENTS (350 words):
- Personal, relatable opening
- Story or journey narrative
- Emotional connection points
- Community-building question
- 10-15 mixed hashtags

OUTPUT:
[Caption]

[Hashtags]

Write ONLY the caption and hashtags.""",
    output_key="instagram_content"
)

blog_specialist = LlmAgent(
    name="BlogSpecialist",
    model=GEMINI_TEXT_MODEL,
    description="Long-form content expert.",
    instruction="""You are a blog specialist. Create comprehensive, SEO-optimized articles.

STRUCTURE (800-1500 words):
1. **Title** (SEO-optimized)
2. **Introduction** (Hook, problem, promise)
3. **Main Sections** (3-4 with H2 headers)
4. **Practical Applications**
5. **Conclusion** (Recap and CTA)

Use markdown formatting.

OUTPUT:
# [Title]

[Full article]

Write ONLY the article.""",
    output_key="blog_content"
)


# PATTERN 3: REFLECTION - Quality Assessment
quality_reflector = LlmAgent(
    name="QualityReflector",
    model=GEMINI_TEXT_MODEL,
    description="Quality assessment and improvement specialist.",
    instruction="""You are a quality assessment specialist. Evaluate content quality and suggest improvements.

EVALUATION CRITERIA:
1. **Platform Fit** (1-10): Does content match platform requirements?
2. **Engagement Potential** (1-10): Will this drive interaction?
3. **Research Integration** (1-10): How well is data incorporated?
4. **Brand Consistency** (1-10): Message alignment across platforms?
5. **Value Delivery** (1-10): Does this provide real value?

OUTPUT FORMAT:
**QUALITY ASSESSMENT**

**Overall Score**: [Average score]/10

**Platform-Specific Scores**:
- [Platform]: [Score]/10 - [Brief assessment]

**Strengths**:
- [Key strength points]

**Improvement Areas**:
- [Specific suggestions]

**Research Integration**: [How well current information is used]

**Final Verdict**: [Ready for publication / Needs revision]""",
    output_key="quality_assessment"
)

content_refiner = LlmAgent(
    name="ContentRefiner",
    model=GEMINI_TEXT_MODEL,
    description="Final content refinement specialist.",
    instruction="""You are a content refinement specialist. Apply quality improvements and create final package.

Based on quality assessment, refine content where needed and present the final deliverable.

OUTPUT FORMAT:
**=== ENHANCED CONTENT PACKAGE ===**

**STRATEGY OVERVIEW**
- Platforms: [Selected platforms]
- Research Integration: [How research enhanced content]
- Optimization Applied: [Key improvements made]

**FINAL CONTENT**

[Present refined content for each platform]

**QUALITY METRICS**
- Overall Quality: [Score]/10
- Ready for Publication: [Yes/No]

**DEPLOYMENT NOTES**
- Best posting times
- Cross-promotion strategy
- Performance tracking recommendations""",
    output_key="final_enhanced_package"
)


# Sequential Pipeline Assembly
content_pipeline = SequentialAgent(
    name="ResearchEnhancedPipeline",
    sub_agents=[
        routing_agent,
        x_specialist,
        linkedin_specialist,
        instagram_specialist,
        blog_specialist,
        quality_reflector,
        content_refiner
    ],
    description="Complete pipeline with routing, parallel creation, and reflection."
)


async def create_content(request: str) -> str:
    """
    Execute research-enhanced content pipeline.
    
    This demonstrates all three patterns:
    1. ROUTING - Smart request analysis
    2. PARALLELIZATION - Multiple platform specialists (sequential for free tier)
    3. REFLECTION - Quality assessment and refinement
    """
    # This would be executed through the standard pipeline
    return await create_smart_routed_content(request)


from .smart_routing import create_smart_routed_content