#!/usr/bin/env python3
import os
import json
import random

os.system("clear")

with open("data/slowka.json", "r") as f:
    data = json.load(f)


units = {unit: [category for category in data[unit]] for unit in data}

print("\033[92mPick unit\033[0m\n")

for i, unit in zip(range(len(units.keys())), units.keys()):
	print("\033[92m{}\033[0m. {}".format(i+1, unit))

picked_unit = list(units.keys())[int(input("\n\033[92mUnit\033[0m: "))-1]

os.system("clear")
print("\033[92mPick categories\033[0m\n")

for i, category in zip(range(len(units[picked_unit])), units[picked_unit]):
    print("\033[92m{}\033[0m. {}".format(i+1, category))

questions = []
picked_category = input("\n\033[92mCategories\033[0m [x/x-y/*]: ")
picked_category = picked_category.split("-")

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

points = 0

counter = 1
while questions:
	os.system("clear")
	i = random.randrange(0, len(questions))
	question = questions[i]

	print("\033[93m#\033[0m{}/{} \033[93m{}\033[0m".format(counter, word_amount, question["category"]))
	print("\033[91mPoints: {:.2f}\033[0m\n".format(points))
	print("\033[91m Polish\033[0m  : {}".format(question["pl"]))
	answer = input("\033[96m English\033[0m : ").strip().lower()
	
	if question["eng"] == answer:
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