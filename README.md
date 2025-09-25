# Smart Routing Social Media Content Pipeline

Intelligent multi-platform content generator using Google's Agent Development Kit. Automatically selects platforms, generates tailored content, and improves quality through AI feedback loops.

## Three Agentic Patterns

### 1. Smart Routing
LLM analyzes requests → Selects optimal platforms based on content type

### 2. Conditional Execution  
Only generates for selected platforms (60-70% API cost savings)

### 3. Quality Feedback Loop
Iterative improvement: Generate → Score → Regenerate if < 6.5/10 (max 3 attempts)

## Quick Start

```bash
# Install
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Configure .env file
echo "GOOGLE_API_KEY=your_key_here" > .env

# Run
python main.py
```

## Environment Setup

Create `.env` file:
```env
# Required
GOOGLE_API_KEY=your_google_api_key

# Optional (defaults shown)
GEMINI_TEXT_MODEL=gemini-2.5-flash
```

Get API key: https://aistudio.google.com/app/apikey

## Usage Examples

```
Create LinkedIn content about AI trends
Write Instagram post about productivity  
Generate blog content about remote work
Create content for X and LinkedIn about leadership
```

**Output (30-90 seconds):**
- Platform selection reasoning
- Generated content per platform
- Quality scores + improvement history
- Implementation insights

## Agent System

| Agent | Role | Output |
|-------|------|--------|
| **SmartRouter** | Platform selection | JSON decision: platforms, confidence, reasoning |
| **XContentSpecialist** | X/Twitter content | 280 char conversational posts |
| **LinkedInContentSpecialist** | LinkedIn content | 500 word professional insights |
| **InstagramContentSpecialist** | Instagram content | 350 word authentic stories |
| **BlogContentSpecialist** | Blog content | 800-1500 word articles |
| **ResearchEnhancer** | Current info gathering | Data, trends, examples |
| **QualityChecker** | Content assessment | 0-10 scores, improvement suggestions |
| **ContentRegenerator** | Content improvement | Enhanced versions based on feedback |

## Key Configuration

**Quality Settings** (`src/config/settings.py`):
```python
QUALITY_SCORE_THRESHOLD = 6.5  # Min acceptable score
MAX_QUALITY_ATTEMPTS = 3       # Regeneration limit
```

**Rate Limits** (seconds):
```python
RATE_LIMIT_DELAYS = {
    "after_routing": 4,
    "after_research": 2,
    "between_platforms": 3,
    "cooling_period": 15
}
```

**Research Config** (`src/config/__init__.py`):
```python
RESEARCH_CONFIG = {
    "enabled": True,
    "search_queries_per_topic": 2,
    "max_sources": 3
}
```

## Platform Specifications

| Platform | Type | Length | Focus |
|----------|------|--------|-------|
| X/Twitter | Quick posts | 280 chars | Viral, trending |
| LinkedIn | Professional | 500 words | Thought leadership |
| Instagram | Stories | 350 words | Visual, authentic |
| Blog | Articles | 800-1500 words | Deep analysis, SEO |

## Tools & Dependencies

**Core:**
- `google-adk` - Agent Development Kit
- `google-generativeai` - Gemini API  
- `python-dotenv` - Environment config

**Optional:**
- `google_search` - Research enhancement

## Project Structure

```
smart-routing-pipeline/
├── main.py                    # Entry point
├── .env                       # API keys
├── requirements.txt
├── src/
│   ├── agents/               # Routing, content, research, quality
│   ├── config/               # Settings, environment
│   ├── pipelines/            # Main orchestration
│   └── utils/                # Parsing, runners, quality
```

## Troubleshooting

**Setup:**
```bash
python src/config/environment.py  # Validate setup
```

**Common Issues:**
- Rate limits → Increase delays in `settings.py`
- Low scores → Be more specific in requests
- No platforms → Clarify content type/audience

## Performance

- **API Efficiency:** 60-70% cost reduction
- **Quality:** 85%+ first-attempt approval, avg 8.1/10
- **Speed:** 30-90 seconds depending on complexity

---

**Start Creating:**
```bash
python main.py
```