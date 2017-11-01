#!/usr/bin/env python3
import json
import os
import random

import colored
from colored import stylize


def colored_print(text, color='light_green', **kwargs):
    print(stylize(text, colored.fg(color)), **kwargs)  # NOQA


def pick_unit():
    while True:
        try:
            value = input(stylize('Unit: ', colored.fg('light_green')))
            value = int(value) - 1
            # TODO exception
            return list(units.keys())[value]
        except (ValueError, KeyError):
            print("(E) wrong value, try again")


def pick_category():
    while True:
        try:
            category = input(stylize('Categories', colored.fg('light_green')) + ' [x/x-y/*]: ')

            assert category, 'Invalid category'
            return category.split('-')
        except AssertionError:
            print('(E) wrong value, try again')


def read_answer(text, color):
    while True:
        try:
            answer = input(stylize(text, colored.fg(color)) + ' : ')
            answer = answer.strip().lower()

            assert answer, 'You have to pass a string value'
            return answer
        except AssertionError as e:
            print('(E) wrong value, try again (%s)' % e)


questions = []
points = 0

# Load data
with open('data/data.json', 'r') as f:
    data = json.load(f)
units = {unit: [category for category in data[unit]] for unit in data}

## Units

os.system('cls||clear')
colored_print('Pick unit', end='\n\n')

# List units
for i, unit in enumerate(units.keys()):
    colored_print(i + 1, end='')
    print('. %s' % unit)
print('\n')

picked_unit = pick_unit()

## Categories

os.system('cls||clear')
colored_print('Pick categories', end='\n\n')

# List categories
for i, category in zip(range(len(units[picked_unit])), units[picked_unit]):
    colored_print(i + 1, end='')
    print('. %s' % category)
print ('\n')

picked_category = pick_category()

# Prepare words
if len(picked_category) > 1:
	part = slice(int(picked_category[0])-1, int(picked_category[1]))
elif picked_category[0] == '*':
	part = slice(0, len(units[unit]))
else:
	part = slice(int(picked_category[0])-1, int(picked_category[0]))

for category in units[picked_unit][part]:
	for word in data[picked_unit][category]:
		word['category'] = category
		word['points'] = 1
		questions.append(word)

word_amount = len(questions)

## Quiz

counter = 1
while questions:
    os.system('cls||clear')
    i = random.randrange(0, len(questions))
    question = questions[i]

    colored_print('#', 'light_yellow', end='')
    print('%s/%s '  % (counter, word_amount), end='')
    colored_print(question['category'], 'light_yellow')

    colored_print('Points: %.2f' % points, 'red', end='\n\n')

    colored_print('> Polish ', 'light_red', end='')
    print(':  %s' % question['pl'])

    def process_answer(answer):
        global counter
        global points
        print('')

        if question['eng'].strip().lower() == answer:
            counter += 1
            points += question['points']

            colored_print('> Correct [+%.2f] point(s)' % question['points'])
            questions.pop(i)
            return True
        else:
            colored_print('> Wrong, ', 'light_red', end='')
            print('the answer is: ', end='')
            colored_print(question['eng'], 'light_yellow')
            print('> Type it in.', end='\n\n')

            questions[i]['points'] /= 2
            return False

    while True:
        answer = read_answer('> English', 'light_cyan')
        if process_answer(answer):
            break

    input()
