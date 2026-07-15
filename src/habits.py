#!/usr/bin/env python3

# DOCKS
from pathlib import Path
from datetime import date
import json
import sys
import os
import platformdirs
if os.name != "nt":
    import readline

__version__ = "v0.1"

# FILES
DATA_DIR = platformdirs.user_data_dir("afterPunch/habits")
DATA_LOCATION = f"{DATA_DIR}/habits.json"

Path(DATA_DIR).mkdir(exist_ok=True)

# FUNCTIONS
## CORE
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def confirm(msg="Are you sure?") -> bool:
    while True:
        choice = input(f"{msg} [Y/n] ").strip().lower()
        if "n" in choice:
            return False
        elif "y" in choice or not choice:
            return True
        else:
            print("ERROR: Invalid choice")
            continue

def close(code=0):
    global habits
    if habits:
        save()
    sys.exit(code)

## PROGRAM SPECIFIC
def add(name=None, cat="uncategorized", status="incomplete") -> str:
    if name is None:
        name = f"HABIT{len(habits)+1}"
    habits[name] = {
        "category": cat,
        "status": status,
        "created_at": date.today().isoformat(),
    }
    return "Added!"

def rem(name) -> str:
    if name in habits and confirm(f"You wanna remove {name}?"):
        del habits[name]
        return f"Removed {name}!"
    return f"ERROR: Couldn't remove {name}!"

def save() -> str:
    with open(DATA_LOCATION, "w") as d:
        json.dump(habits, d, indent=4)
    return "Data Saved!"

def fetch() -> dict:
    if Path(DATA_LOCATION).exists():
        with open(DATA_LOCATION, "r") as d:
            return json.load(d)
    else:
        return {}

def show():
    for name, data in habits.items():
        print(name)
        for k, v in data.items():
            print(f"- {k}: {v}")
    print()

def update(name, item, new_value) -> str:
    if name in habits and confirm(f"Update {habits[name[item]]} to {new_value}? "):
        habits[name][item] = new_value
        return "Updated!"
    return "Failed!"

def main():
    global habits
    habits = fetch()

    while True:
        ui = input("󰘧 ").strip().split()
        if not ui:
            continue
        cmd = ui[0].lower()

        if cmd in {"cls", "clear"}:
            clear()

        elif cmd in {"exit", "quit", "q"}:
            close()

        elif cmd == "add":
            add(ui[1], ui[2], ui[3])

        elif cmd == "rem":
            rem(ui[1])

        elif cmd == "update":
            update(ui[1], ui[2], ui[3])

        elif cmd == "save":
            save()

        elif cmd == "load":
            habits = fetch()

        elif cmd == "show":
            show()
        
        else:
            print("ERROR: Invalid command!")

if __name__ == "__main__":
    main()

# END OF LINE
