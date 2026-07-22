#!/usr/bin/env python3

# === INIT ===
from pathlib import Path
from datetime import date
import json
import sys
import os
import platformdirs
import bolts

__version__ = "v0.1.1"

# === FILES ===
DATA_DIR = platformdirs.user_data_dir("afterPunch/habits")
DATA_LOCATION = f"{DATA_DIR}/habits.json"

Path(DATA_DIR).mkdir(exist_ok=True)

# === PROGRAM FUNCTIONS ===
def add(name=None, cat="uncategorized", status="incomplete"):
    if name is None:
        name = f"HABIT{len(habits)+1}"
    habits[name] = {
        "category": cat,
        "status": status,
        "created_at": date.today().isoformat(),
    }
    print(f"{bolts.GREEN}INFO{bolts.RST}: Data added")

def rem(name):
    if name in habits and bolts.confirm(f"Permanently delete {name}?"):
        del habits[name]
        print(f"{bolts.GREEN}INFO{bolts.RST}: Removed {name}")
        return
    bolts.error(6)

def save():
    with open(DATA_LOCATION, "w") as d:
        json.dump(habits, d, indent=4)
    print(f"{bolts.GREEN}INFO{bolts.RST}: Data saved")

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

def update(name, item, new_value):
    if name in habits and bolts.confirm(f"Update {habits[name][item]} to {new_value}? "):
        habits[name][item] = new_value
        print(f"{bolts.GREEN}INFO{bolts.RST}: Updated")
    bolts.error(8)

# === PUTTING IT ALL TOGETHER ===
def main():
    global habits
    habits = fetch()

    while True:
        ui = input(f"{bolts.MAGENTA}󰘧{bolts.RST} ").strip().split()
        if not ui:
            continue
        cmd = ui[0].lower()

        if cmd in {"cls", "clear", "c"}:
            bolts.clear()

        elif cmd in {"exit", "quit", "q"}:
            bolts.close(func=save, condition=habits)

        elif cmd == "add":
            try:
                add(ui[1], ui[2], ui[3])
            except IndexError:
                bolts.error(3)

        elif cmd == "rem":
            try:
                rem(ui[1])
            except IndexError:
                bolts.error(3)

        elif cmd == "update":
            try:
                update(ui[1], ui[2], ui[3])
            except IndexError:
                bolts.error(3)

        elif cmd == "save":
            save()

        elif cmd == "load":
            habits = fetch()

        elif cmd == "show":
            show()
        
        else:
            bolts.error(10)

if __name__ == "__main__":
    main()

# === END OF LINE ===
