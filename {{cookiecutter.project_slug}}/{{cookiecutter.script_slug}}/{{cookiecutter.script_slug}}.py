import platform
import os
from _version import __version__
import pandas as pd


# Get the users home directory
if platform.system() == "Windows":
    from pathlib import Path

    homedir = str(Path.home())
else:
    homedir = os.environ['HOME']


def main(arg_1, arg_2):
    """
    Main method for script...
    """
    pass