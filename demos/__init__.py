"""
Demo scripts for Smart Routing Pipeline
Various demonstrations of pipeline capabilities
"""

from .simple_demo import simple_demo, platform_specific_demo, multi_platform_demo
from .pattern_showcase import AgenticPatternsDemo
from .interactive import interactive_cli

__all__ = [
    "simple_demo",
    "platform_specific_demo", 
    "multi_platform_demo",
    "AgenticPatternsDemo",
    "interactive_cli"
]