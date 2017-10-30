#!/usr/bin/env python3
import json
import os
import random

import colored
from colored import stylize


def colored_print(text, color="light_green", **kwargs):
    print(stylize(text, colored.fg(color)), **kwargs)  # NOQA


def pick_unit():
    while True:
        try:
            value = input(stylize("Unit: ", colored.fg("light_green")))
            value = int(value) - 1
            # TODO exception
            return list(units.keys())[value]
        except (ValueError, KeyError):
            print("(E) wrong value, try again")


def pick_category():
    picked_category = input(stylize("Categories", colored.fg("light_green")) + " [x/x-y/*]: ")
    return picked_category.split("-")


questions = []
points = 0

# Load data
with open("data/slowka.json", "r") as f:
    data = json.load(f)
units = {unit: [category for category in data[unit]] for unit in data}

## Units

os.system('cls||clear')
colored_print("Pick unit", end="\n\n")

# List units
for i, unit in enumerate(units.keys()):
    colored_print(i + 1, end='')
    print(". {}".format(unit))
print()

picked_unit = pick_unit()

## Categories

os.system('cls||clear')
colored_print("Pick categories", end="\n\n")

# List categories
for i, category in zip(range(len(units[picked_unit])), units[picked_unit]):
    colored_print(i + 1, end='')
    print(". {}".format(category))
print()

picked_category = pick_category()

# Prepare words
if len(picked_category) > 1:
	part = slice(int(picked_category[0])-1, int(picked_category[1]))
elif picked_category[0] == "*":
	part = slice(0, len(units[unit]))
else:
	part = slice(int(picked_category[0])-1, int(picked_category[0]))

for category in units[picked_unit][part]:
	for word in data[picked_unit][category]:
		word["category"] = category
		word["points"] = 1
		questions.append(word)

word_amount = len(questions)

## Quiz

counter = 1
while questions:
	os.system('cls||clear')
	i = random.randrange(0, len(questions))
	question = questions[i]

	print("\033[93m#\033[0m{}/{} \033[93m{}\033[0m".format(counter, word_amount, question["category"]))
	print("\033[91mPoints: {:.2f}\033[0m\n".format(points))
	print("\033[91m Polish\033[0m  : {}".format(question["pl"]))
	answer = input("\033[96m English\033[0m : ")

	if question["eng"].strip().lower() == answer.strip().lower():
		counter += 1
		points += question["points"]
		print("\n \033[92mCorrect [+{:.2f} point]\033[0m".format(question["points"]))
		questions.pop(i)
	else:
		print("\n \033[91mWrong\033[0m [\033[93m{}\033[0m]\n".format(question["eng"]))
		questions[i]["points"] /= 2
		while answer != question["eng"]:
			answer = input("\033[96m Again\033[0m : ").strip().lower()

	input()
