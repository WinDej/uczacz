import os
import colored
from colored import stylize


def clear_view():
    os.system('cls||clear')


def colored_print(text, color='light_green', **kwargs):
    print(stylize(text, colored.fg(color)), **kwargs)  # NOQA
