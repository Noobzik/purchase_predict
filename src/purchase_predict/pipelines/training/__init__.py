"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.19.10
"""

from .pipeline import create_pipeline
from dotenv import load_dotenv


__all__ = ["create_pipeline"]

__version__ = "0.1"
load_dotenv()
