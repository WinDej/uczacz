#!/usr/bin/env python3
import json

with open("data/slowka.json", "r") as f:
    data = json.load(f)

if len(data["unit1"]) > 0:
    counter = len(data["unit1"])-1
    print("{}. \033[94m{}\033[0m - \033[91m{}\033[0m".format(counter, data["unit1"][-1]["eng"], data["unit1"][-1]["pl"]))
else:
    counter = 0

while True:
    counter += 1
    print("\n{}. ".format(counter), end="")
    data["unit1"].append({"eng": input("\t\033[94mEnglish\033[0m : ").strip(), 
                            "pl":  input("\t\033[91mPolish\033[0m  : ").strip() 
                        })

    with open("slowka.json", "w") as f:
        json.dump(data, f, indent = 2)
