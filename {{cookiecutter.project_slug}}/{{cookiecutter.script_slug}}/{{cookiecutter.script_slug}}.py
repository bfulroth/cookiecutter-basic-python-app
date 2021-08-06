"""Main method and helper methods for {{cookiecutter.script_slug}}.py"""

# Import the version of the script that can be used to tag the output file.
from _version import __version__

# Import system packages for determining what OS the script is running on..
import platform
import os

# Import data wrangling Python packages
import pandas as pd
import numpy as np

# Import utility packages
import logging

# Set the date to include in the file directory if a crash occures
NOW = datetime.now()
NOW = NOW.strftime('%y%m%d')

# Configure logger
logging.basicConfig(level=logging.INFO)

# Get the users home directory
if platform.system() == "Windows":
    from pathlib import Path

    homedir = str(Path.home())
else:
    homedir = os.environ['HOME']


def main(arg_1, arg_2, flag):
    """
    Main method for script...
    """
    pass