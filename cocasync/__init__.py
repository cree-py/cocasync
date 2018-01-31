from .client import *

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../version.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    version = f.read()

__author__ = 'Umbresp'
__title__ = 'cocasync'
__license__ = 'MIT'
__version__ = version
__github__ = 'https://www.github.com/cree-py/cocasync'