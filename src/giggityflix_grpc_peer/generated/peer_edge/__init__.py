# Import the local pb2 module BEFORE anything else
import sys
import os
from pathlib import Path

# Get the current directory path
_current_dir = str(Path(__file__).parent)

# Add current directory to sys.path temporarily (if not already there)
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)