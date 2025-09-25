"""
Pipeline orchestration for Smart Routing System
Manages execution flow and agent coordination
"""

from .smart_routing import create_smart_routed_content
from .research_enhanced import create_content

__all__ = [
    "create_smart_routed_content",
    "create_content"
]