"""
Entry point for Gesture-Driven Spotify Control.
Run this file from the project root: python run.py
"""
import sys
import os

# Add src/ to Python path so internal imports resolve correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from main import main  # noqa: E402

if __name__ == "__main__":
    main()
