# === DOCKS ===
from .feels import *
import os
import sys
import platform
if os.name != "nt": import readline

# === HEART ===
def get_os() -> str:
    os = platform.system()
    if os == "Darwin":
        os = "macOS"
    return os

def clear():
    os.system("cls" if get_os() == "Windows" else "clear")

# === ERRORS ===
ERRORS = {
    1 : "Invalid input",
    2 : "Missing input",
    3 : "Out of range",
    4 : "File not found",
    5 : "File already exists",
    6 : "Permission denied",
    7 : "Invalid or missing config",
    8 : "Operation failed",
    9 : "Unknown error",
    10: "Invalid command"
}

def error(code=9):
    print(f"{RED}ERR_{code}{RST}: {ERRORS[code]}")

# === OTHER FUNCTIONS ===
def confirm(msg="You sure? ", blank=True) -> bool:
    while True:
        choice = input(f"{msg} [Y/n] ").strip().lower()
        if "n" in choice:
            return False
        elif "y" in choice or (not choice and blank):
            return True
        else:
            error(1)

def close(code=0, func=None, condition=None):
    if func and condition:
        func()
    sys.exit(code)

# === END OF LINE ===

