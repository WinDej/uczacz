#!/usr/bin/env python3
import os
import json
import random

os.system("clear")

with open("data/slowka.json", "r") as f:
    data = json.load(f)
    data = data["unit1"]


categories = [c for c in data]

for i, category in zip(range(len(categories)), categories):
    print("\033[92m{}\033[0m. {}".format(i+1, category))

questions = []
picked = input("\033[92mCategory\033[0m: ")
picked = picked.split("-")

if len(picked) > 1:
	s = slice(int(picked[0])-1, int(picked[1]))
elif picked[0] == "*":
	s = slice(len(categories))
else:
	s = slice(int(picked[0])-1, int(picked[0]))

for category in categories[s]:
	for word in data[category]:
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