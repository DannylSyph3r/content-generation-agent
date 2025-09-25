"""
Smart Routing Social Media Content Pipeline
Source code package for intelligent content generation
"""

__version__ = "5.0.0"
__author__ = "Smart Routing Pipeline"

# Package initialization
from . import agents
from . import config
from . import pipelines
from . import utils

__all__ = [
    "agents",
    "config", 
    "pipelines",
    "utils"
]