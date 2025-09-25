# Smart Routing Social Media Content Pipeline

An intelligent social media content generation pipeline using Google's Agent Development Kit (ADK). Features smart platform routing, research enhancement, and quality feedback loops for optimal content creation.

## Key Features

- **Smart Platform Routing** - Automatically selects optimal platforms for your content
- **Conditional Execution** - Only generates content for selected platforms (saves API calls)
- **Research Enhancement** - Integrates current information and trends
- **Quality Feedback Loop** - Iterative improvement until quality standards are met
- **Platform Specialization** - Optimized content for each platform's unique requirements

## Quick Start

### 1. Setup Environment

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API key
echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
```

### 2. Verify Configuration

```bash
python src/config/environment.py
```

Expected output:
```
>> Google ADK imported successfully
>> GOOGLE_API_KEY configured
>> GEMINI_TEXT_MODEL: gemini-2.5-flash
Environment validation successful!
```

### 3. Run the Pipeline

```bash
python main.py
```

That's it! The interactive interface will guide you through creating content.

## Usage Examples

Once you run `main.py`, you can enter requests like:

### Single Platform Content
```
Create LinkedIn content about AI in healthcare
Write an Instagram post about morning productivity tips
Generate X content about sustainable technology innovations
Create a blog post about remote work best practices
```

### Multi-Platform Content
```
Create content for LinkedIn and Instagram about leadership skills
Write content for X and LinkedIn about the future of work
Generate Instagram and blog content about sustainable living
```

### Research-Enhanced Content
```
Write about the latest trends in electric vehicles
Create content about recent developments in AI technology
Generate content about current sustainable energy innovations
```

The pipeline will:
1. Analyze your request
2. Select optimal platforms
3. Gather current research
4. Generate platform-optimized content
5. Apply quality improvements
6. Deliver publication-ready results

## Supported Platforms

| Platform | Content Type | Character/Word Limit | Optimization Focus |
|----------|--------------|---------------------|-------------------|
| **X/Twitter** | Quick, engaging posts | 280 characters | Hooks, hashtags, CTAs |
| **LinkedIn** | Professional thought leadership | ~500 words | Business insights, industry analysis |
| **Instagram** | Authentic storytelling | ~350 words | Visual-first, community building |
| **Blog** | Comprehensive articles | 800-1500 words | SEO optimization, deep analysis |

## How It Works

### 1. Smart Routing
The routing agent analyzes your request to determine:
- Content type and complexity
- Optimal platform(s) for your message
- Whether clarification is needed
- Research requirements

### 2. Research Enhancement
When beneficial, the system:
- Gathers current information
- Identifies relevant trends
- Integrates factual data
- Enhances content accuracy

### 3. Content Generation
Platform specialists create optimized content:
- Platform-specific tone and style
- Appropriate length and format
- Engagement-optimized structure
- Audience-appropriate language

### 4. Quality Assessment
Content undergoes evaluation for:
- Platform fit (1-10 score)
- Engagement potential
- Authenticity and human touch
- Value delivery
- Brand consistency

### 5. Iterative Improvement
Based on quality feedback:
- Identifies improvement areas
- Regenerates enhanced content
- Validates against thresholds
- Ensures publication readiness

## Usage Tips

### Getting Better Results

**Be Specific**
- Good: "Create LinkedIn content about AI applications in healthcare diagnostics"
- Avoid: "Write about technology"

**Specify Platforms When Needed**
- "Create LinkedIn content about..." (single platform)
- "Create content for LinkedIn and Instagram about..." (multi-platform)
- Let the system decide if you're unsure

**Trigger Research Enhancement**
- "Latest trends in..."
- "Recent developments in..."
- "Current state of..."

**Multi-Platform Requests**
- Explicitly mention multiple platforms
- System will optimize for each platform's unique requirements

### Understanding Output

The system provides:
- **Platform Selection Reasoning** - Why these platforms were chosen
- **Generated Content** - Actual publication-ready content for each platform
- **Quality Assessment** - Scores and evaluation metrics
- **Implementation Insights** - Tips for optimization and deployment
- **Performance Notes** - Best posting times, cross-promotion strategies

### Common Scenarios

**Ambiguous Requests**
If your request is unclear, the system will ask for clarification rather than making assumptions.

**API Rate Limits**
Built-in cooling periods (15-25 seconds) prevent rate limit issues automatically.

**No Platform Selected**
Refine your request to be more specific about the topic or target audience.

## Project Structure

```
smart-routing-pipeline/
├── main.py                    # Interactive interface (start here)
├── .env                       # API configuration
├── requirements.txt           # Python dependencies
├── src/
│   ├── agents/               # Specialized AI agents
│   │   ├── routing.py        # Smart routing logic
│   │   ├── content.py        # Platform specialists
│   │   ├── research.py       # Research enhancement
│   │   └── quality.py        # Quality assessment
│   ├── config/
│   │   ├── settings.py       # Platform configurations
│   │   └── environment.py    # Environment validation
│   ├── pipelines/
│   │   └── smart_routing.py  # Main pipeline orchestration
│   └── utils/                # Helper functions
└── README.md
```

## Technical Architecture

### Smart Routing Algorithm
```
1. Request Analysis
   ├── Parse user intent
   ├── Identify key topics
   └── Assess complexity

2. Platform Selection
   ├── Evaluate platform compatibility
   ├── Match content type to platform
   └── Determine optimal combination

3. Conditional Execution
   ├── Generate only for selected platforms
   ├── Skip unnecessary API calls
   └── Optimize resource usage
```

### Quality Feedback Loop
```
1. Content Generation
   └── Platform-specific specialists create content

2. Quality Assessment
   ├── Multi-dimensional evaluation
   ├── Score across 5+ criteria
   └── Identify improvement areas

3. Iterative Refinement (up to 3 cycles)
   ├── Apply specific improvements
   ├── Regenerate enhanced content
   └── Validate quality threshold

4. Final Package
   └── Publication-ready content with insights
```

## Performance Characteristics

- **API Efficiency**: 60-70% reduction in API calls vs. brute-force generation
- **Content Quality**: Consistent 8+/10 scores through feedback loops
- **Processing Time**: 30-90 seconds depending on complexity
- **Platform Optimization**: Specialist agents maximize engagement potential

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
GOOGLE_API_KEY=your_google_api_key

# Optional (defaults shown)
GEMINI_TEXT_MODEL=gemini-2.5-flash
```

### Platform Configurations

Platform settings are defined in `src/config/settings.py`:
- Character/word limits
- Style guidelines
- Best practices
- Optimization rules

Modify these to customize platform behavior.

## Troubleshooting

### Setup Issues

**Import Errors**
```bash
pip install -r requirements.txt
```

**API Key Not Found**
```bash
# Verify .env file exists and contains GOOGLE_API_KEY
cat .env
```

**Environment Check Fails**
```bash
python src/config/environment.py
```

### Runtime Issues

**Rate Limits**
The system automatically handles rate limits with cooling periods. If you encounter issues, increase delays in `src/config/settings.py`.

**Low Quality Scores**
Be more specific in your requests. Include context, target audience, and desired tone.

**No Platforms Selected**
Refine your request to be clearer about topic and purpose. The router needs sufficient context.

## Advanced Usage

### Custom Platform Specialists

Add new platforms by creating specialists in `src/agents/content.py`:

```python
custom_specialist = LlmAgent(
    name="CustomPlatformSpecialist",
    model=GEMINI_TEXT_MODEL,
    description="Specialist for custom platform",
    instruction="Your custom instructions...",
    output_key="custom_content"
)
```

### Modify Quality Thresholds

Adjust quality requirements in `src/config/settings.py`:

```python
QUALITY_THRESHOLDS = {
    "minimum_score": 7.0,  # Change as needed
    "max_iterations": 3
}
```

### Research Enhancement

Control research behavior in `src/config/settings.py`:

```python
RESEARCH_CONFIG = {
    "enabled": True,
    "search_queries_per_topic": 2,
    "max_sources": 3
}
```

## Contributing

This project demonstrates advanced agentic patterns for content generation. Areas for contribution:

- **Platform Specialists** - Add support for new social platforms
- **Research Capabilities** - Enhanced information gathering
- **Quality Assessment** - More sophisticated evaluation metrics
- **Performance Optimization** - Faster processing, better caching

## License

Educational and demonstration project showcasing intelligent content generation using Google's Agent Development Kit (ADK).

---

**Get Started Now**

```bash
python main.py
```

Enter a request and experience intelligent, platform-optimized content generation.