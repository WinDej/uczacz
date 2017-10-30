#!/usr/bin/env python3

# TODO move it as part of Uczacz class

import json
import sys

if len(sys.argv) < 3:
	print('Usage: ./insert.py "<unit name>" "<category name>"')
	sys.exit(1)

with open("data/data.json", "r") as f:
    data = json.load(f)

unit = sys.argv[1]
category = sys.argv[2]

if unit not in data.keys():
	data[unit] = {}

if category not in data[unit].keys():
	data[unit][category] = []


if len(data[unit][category]) > 0:
    counter = len(data[unit][category])-1
    print("{}: {}. \033[94m{}\033[0m - \033[91m{}\033[0m".format(category,
    															 counter,
    															 data[unit][category][-1]["eng"],
    															 data[unit][category][-1]["pl"]))
else:
    counter = 0

print("\033[93m{} -> {}\033[0m".format(unit, category))

while True:
    counter += 1
    print("\n{}. ".format(counter), end="")  # NOQA
    data[unit][category].append({"eng": input("\t\033[94mEnglish\033[0m : ").strip(),
                            	 "pl":  input("\t\033[91mPolish\033[0m  : ").strip()
                        })

    with open("data/data.json", "w") as f:
        json.dump(data, f, indent = 2)
