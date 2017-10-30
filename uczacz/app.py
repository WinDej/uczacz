import json
import os
import random

import colored
from colored import stylize
from uczacz import clear_view, colored_print


class Uczacz():
    data = {}

    def __init__(self):
        # TODO argparser
        self.load_data()

    def run(self):
        unit = self.units()
        category, questions = self.categories(unit)

        counter = 1
        points = 0

        while questions:
            os.system('cls||clear')
            i = random.randrange(0, len(questions))
            question = questions[i]

            # header
            colored_print('#', 'light_yellow', end='')
            print('%d/%d ' % (counter, len(questions)), end='')  # NOQA
            colored_print(question['category'], 'light_yellow')

            # points achieved
            colored_print('Points: %.2f' % points, 'red', end='\n\n')

            # question
            colored_print('> Polish ', 'light_red', end='')
            print(':  %s' % question['pl'])

            # answer
            while True:
                if self.process_answer(question, self.read_answer('> English', 'light_cyan')):
                    counter += 1
                    points += question['points']
                    questions.pop(i)
                    break

            input("..")

    def load_data(self, source='data/data.json'):
        '''
        Load data from json file
        '''
        with open(source, 'r') as f:
            self.data = json.load(f)

        self.data_units = {unit: [category for category in self.data[unit]] for unit in self.data}

    def units(self):
        '''
        Show available units and ask to choose one
        '''
        clear_view()
        colored_print('Pick unit', end='\n\n')

        # List units
        for i, unit in enumerate(self.data.keys()):
            colored_print(i + 1, end='')
            print('. %s' % unit)
        print('\n')

        return self.pick_unit()

    def categories(self, unit):
        '''
        Show available categories and ask to choose one
        '''
        clear_view()
        colored_print('Pick categories', end='\n\n')

        # List categories
        for idx, category in zip(range(len(self.data[unit])), self.data[unit]):
            colored_print(idx + 1, end='')
            print('. %s' % category)
        print('\n')

        category = self.pick_category()

        # Parse category input
        # TODO simplify it
        if len(category) > 1:
            selector = slice(int(category[0]) - 1, int(category[1]))
        if category[0] == '*':
            selector = slice(0, len(self.data[unit]))
        else:
            selector = slice(int(category[0]) - 1, int(category[0]))

        questions = []
        for category in self.data_units[unit][selector]:
            for word in self.data[unit][category]:
                word['category'] = category
                word['points'] = 1
                questions.append(word)

        return category, questions

    def process_answer(self, question, answer):
        print('')

        if question['eng'].strip().lower() == answer:
            colored_print('> Correct [+%.2f] point(s)' % question['points'])
            return True
        else:
            colored_print('> Wrong, ', 'light_red', end='')
            print('the answer is: ', end='')
            colored_print(question['eng'], 'light_yellow')
            print('> Type it in.', end='\n\n')

            question['points'] /= 2
            return False

    def pick_unit(self):
        while True:
            try:
                value = input(stylize('Unit: ', colored.fg('light_green')))
                value = int(value) - 1
                return list(self.data.keys())[value]
            except (ValueError, KeyError):
                print("(E) wrong value, try again")


    def pick_category(self):
        while True:
            try:
                category = input(stylize('Categories', colored.fg('light_green')) + ' [x/x-y/*]: ')
                assert category, 'Invalid category'
                return category.split('-')
            except AssertionError:
                print('(E) wrong value, try again')


    def read_answer(self, text, color):
        while True:
            try:
                answer = input(stylize(text, colored.fg(color)) + ' : ')
                answer = answer.strip().lower()

                assert answer, 'You have to pass a string value'
                return answer
            except AssertionError as e:
                print('(E) wrong value, try again (%s)' % e)

