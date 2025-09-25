"""
Quality Assessment Utilities
Functions for parsing quality scores and managing feedback loops
"""
import re
from typing import Dict, Any, Optional, Tuple
from src.config import QUALITY_SCORE_THRESHOLD


def parse_quality_score(quality_result: str) -> float:
    """
    Parse the overall quality score from quality assessment output.
    
    Args:
        quality_result: String output from quality checker agent
        
    Returns:
        Float score between 0.0 and 10.0, or 0.0 if parsing fails
    """
    try:
        # Look for "OVERALL SCORE: X.X/10" or "Overall Score: X/10" patterns
        score_patterns = [
            r"OVERALL SCORE[:\s]+(\d+\.?\d*)/10",
            r"Overall Score[:\s]+(\d+\.?\d*)/10",
            r"Score[:\s]+(\d+\.?\d*)/10"
        ]
        
        for pattern in score_patterns:
            match = re.search(pattern, quality_result, re.IGNORECASE)
            if match:
                score = float(match.group(1))
                return min(max(score, 0.0), 10.0)  # Clamp between 0-10
        
        # Fallback: look for any number followed by /10
        fallback_match = re.search(r"(\d+\.?\d*)/10", quality_result)
        if fallback_match:
            score = float(fallback_match.group(1))
            return min(max(score, 0.0), 10.0)
            
        print("Warning: Could not parse quality score from assessment")
        return 0.0
        
    except (ValueError, AttributeError) as e:
        print(f"Error parsing quality score: {e}")
        return 0.0


def extract_improvement_suggestions(quality_result: str) -> list:
    """
    Extract improvement suggestions from quality assessment output.
    
    Args:
        quality_result: String output from quality checker agent
        
    Returns:
        List of improvement suggestions
    """
    suggestions = []
    
    try:
        # Look for CONTEXTUAL IMPROVEMENTS section
        improvements_match = re.search(
            r"CONTEXTUAL IMPROVEMENTS[^:]*:(.+?)(?=\*\*|$)", 
            quality_result, 
            re.DOTALL | re.IGNORECASE
        )
        
        if improvements_match:
            improvements_text = improvements_match.group(1).strip()
            # Split by numbered items (1., 2., 3.)
            items = re.split(r'\d+\.', improvements_text)
            suggestions = [item.strip() for item in items if item.strip()]
        
        # Fallback: look for Priority Fix
        if not suggestions:
            priority_match = re.search(
                r"PRIORITY FIX[^:]*:(.+?)(?=\*\*|$)",
                quality_result,
                re.DOTALL | re.IGNORECASE
            )
            if priority_match:
                suggestions = [priority_match.group(1).strip()]
    
    except Exception as e:
        print(f"Error extracting improvement suggestions: {e}")
    
    return suggestions


def format_regeneration_prompt(original_content: str, quality_feedback: str, attempt: int) -> str:
    """
    Format a regeneration prompt that includes original content and quality feedback.
    
    Args:
        original_content: The original content that needs improvement
        quality_feedback: Quality assessment feedback
        attempt: Current attempt number (for context)
        
    Returns:
        Formatted prompt for content regeneration
    """
    prompt = f"""CONTENT REGENERATION REQUEST (Attempt {attempt}/3)

ORIGINAL CONTENT TO IMPROVE:
{original_content}

QUALITY ASSESSMENT FEEDBACK:
{quality_feedback}

Please regenerate this content to address the specific issues identified in the quality assessment. Focus on making it sound more human and natural while maintaining the core message and platform requirements."""

    return prompt


def is_score_acceptable(score: float, threshold: float = QUALITY_SCORE_THRESHOLD) -> bool:
    """
    Check if a quality score meets the acceptance threshold.
    
    Args:
        score: Quality score to check
        threshold: Minimum acceptable score (default from settings.py)
        
    Returns:
        True if score is acceptable, False otherwise
    """
    return score >= threshold


def should_retry_generation(score: float, attempt: int, max_attempts: int = 3, 
                           threshold: float = QUALITY_SCORE_THRESHOLD) -> bool:
    """
    Determine if content generation should be retried based on score and attempt count.
    
    Args:
        score: Current quality score
        attempt: Current attempt number (1-indexed)
        max_attempts: Maximum allowed attempts
        threshold: Minimum acceptable score (default from settings.py)
        
    Returns:
        True if should retry, False if should stop
    """
    return score < threshold and attempt < max_attempts


def format_final_result_with_attempts(content: str, scores_history: list, attempts: int) -> str:
    """
    Format final result including attempt history for transparency.
    
    Args:
        content: Final content
        scores_history: List of scores from each attempt
        attempts: Number of attempts made
        
    Returns:
        Formatted final result with attempt history
    """
    final_score = scores_history[-1] if scores_history else 0.0
    threshold = QUALITY_SCORE_THRESHOLD
    
    result = f"""**=== FINAL CONTENT WITH QUALITY ASSURANCE ===**

**QUALITY OPTIMIZATION SUMMARY**
- Attempts Made: {attempts}
- Final Score: {final_score:.1f}/10
- Score History: {' → '.join(f'{s:.1f}' for s in scores_history)}
- Status: {"✅ APPROVED" if final_score >= threshold else "⚠️ BEST EFFORT (Under Threshold)"}

**FINAL CONTENT**
{content}

**QUALITY NOTES**
{"This content meets quality standards and is ready for publication." if final_score >= threshold else "This content was improved through multiple iterations but may need manual review before publication."}
"""
    
    return result