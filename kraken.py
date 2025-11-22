import os
import sys
import time
import random
import subprocess


if sys.version_info < (3, 0):
    print("This script requires Python 3.")
    sys.exit(1)


try:
    from rich.console import Console
    from rich.table import Table
    from rich.box import SIMPLE_HEAVY
    from colorama import Fore
except ImportError as e:
    print(f"Error: {e}. Please install the required modules using:")
    print("pip install -r requirements.txt")
    sys.exit(1)

console = Console()

def clearScr():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = r""" 

        ▄█   ▄█▄    ▄████████    ▄████████    ▄█   ▄█▄    ▄████████ ███▄▄▄▄   
        ███ ▄███▀   ███    ███   ███    ███   ███ ▄███▀   ███    ███ ███▀▀▀██▄ 
        ███▐██▀     ███    ███   ███    ███   ███▐██▀     ███    █▀  ███   ███ 
        ▄█████▀     ▄███▄▄▄▄██▀   ███    ███  ▄█████▀     ▄███▄▄▄     ███   ███ 
        ▀▀█████▄    ▀▀███▀▀▀▀▀   ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ███   ███ 


