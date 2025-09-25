# Smart Routing Social Media Content Pipeline - Demo Guide

This project demonstrates an intelligent social media content generation pipeline using Google's Agent Development Kit (ADK). The system features smart platform routing, research enhancement, and quality feedback loops.

## Key Features

- **Smart Platform Routing**: Automatically selects optimal platforms for your content
- **Conditional Execution**: Only generates content for selected platforms (saves API calls)
- **Research Enhancement**: Integrates current information and trends
- **Quality Feedback Loop**: Iterative improvement until quality standards are met
- **Platform Specialization**: Optimized content for each platform's unique requirements

## Quick Start

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "GOOGLE_API_KEY=your_actual_api_key_here" > .env
```

### 2. Verify Setup

```bash
python src/config/environment.py
```

### 3. Run the Pipeline

```bash
# Interactive interface (recommended)
python main.py

# Or run demos
python demos/simple_demo.py
python demos/pattern_showcase.py
```

## Demo Options

### Interactive Interface (`main.py`)
The main interactive interface where you can:
- Enter any content request
- See intelligent platform selection in action
- Get research-enhanced, quality-optimized content
- Learn through usage with pro tips

**Example requests:**
- "Create LinkedIn content about AI in healthcare"
- "Write Instagram and X content about productivity"
- "Generate a blog post about sustainable technology"

### Simple Demo (`demos/simple_demo.py`)
Choose from focused demonstrations:
1. **Simple Demo** - Basic smart routing functionality
2. **Platform-Specific Demo** - Platform optimization showcase
3. **Multi-Platform Demo** - Multiple platform routing
4. **Research Enhancement Demo** - Current information integration
5. **Comprehensive Demo** - All features combined

### Pattern Showcase (`demos/pattern_showcase.py`)
Advanced demonstration highlighting:
- Intelligent platform selection patterns
- Research enhancement integration
- Quality feedback loop mechanics
- Conditional execution efficiency

## Supported Platforms

| Platform | Content Type | Optimization |
|----------|--------------|--------------|
| **X/Twitter** | Quick, engaging posts (280 chars) | Trending hashtags, hooks, CTAs |
| **LinkedIn** | Professional thought leadership (500 words) | Business insights, industry focus |
| **Instagram** | Authentic storytelling (350 words) | Visual-first, community building |
| **Blog** | Comprehensive articles (800-1500 words) | SEO optimization, deep analysis |

## Project Structure

```
smart-routing-pipeline/
├── main.py                 # Interactive interface
├── demos/
│   ├── simple_demo.py     # Basic functionality demos
│   └── pattern_showcase.py # Advanced pattern demonstrations
├── src/
│   ├── agents/            # Specialized AI agents
│   ├── config/            # Configuration and environment
│   ├── pipelines/         # Main pipeline logic
│   └── utils/             # Helper functions
└── requirements.txt       # Python dependencies
```

## How It Works

1. **Request Analysis**: Smart router analyzes your request to understand intent and scope
2. **Platform Selection**: Determines which platforms would be most effective
3. **Research Enhancement**: Gathers current information to enhance content relevance
4. **Content Generation**: Specialized agents create platform-optimized content
5. **Quality Assessment**: Evaluates content and applies improvements
6. **Final Package**: Delivers publication-ready content with insights

## Usage Tips

### Getting Better Results
- **Be specific about your topic**: "AI in healthcare" vs "technology"
- **Mention platforms if you have preferences**: "Create LinkedIn content about..."
- **Ask for current information**: "Latest trends in..." triggers research enhancement
- **Request multiple platforms**: "Create content for LinkedIn and Instagram about..."

### Understanding Output
- The pipeline shows its decision-making process
- Platform selection is explained with reasoning
- Quality scores help you understand content strength
- Implementation insights guide optimization

### Common Issues
- **API Rate Limits**: Built-in cooling periods handle this automatically
- **Ambiguous Requests**: System will ask for clarification
- **No Platform Selection**: Refine your request to be more specific

## Technical Details

### Smart Routing Algorithm
1. Analyzes request semantics and intent
2. Evaluates platform compatibility matrix
3. Assesses content complexity requirements
4. Determines optimal platform combination
5. Executes conditional generation workflow

### Quality Feedback Loop
1. Multi-dimensional content assessment
2. Platform-fit evaluation scoring
3. Engagement potential analysis
4. Iterative improvement application
5. Publication readiness verification

### Research Enhancement
- Integrates current information when beneficial
- Enhances content relevance and accuracy
- Provides trend-aware insights
- Maintains factual correctness

## Performance Metrics

- **API Efficiency**: 60-70% reduction in unnecessary API calls through smart routing
- **Content Quality**: Consistent 8+ quality scores through feedback loops
- **Platform Optimization**: Specialized agents achieve higher engagement potential
- **Processing Time**: 30-90 seconds depending on complexity and platform count

## Contributing

This project demonstrates advanced agentic patterns for content generation. Key areas for contribution:
- Additional platform specialists
- Enhanced research capabilities
- Quality assessment improvements
- Performance optimizations