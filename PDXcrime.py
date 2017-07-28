"""
Offers various summations of crime data from Portland, Oregon during the years 2011-2014
Gives user options for the most and least of any option, like zip code or year

"""
from collections import Counter
import os


CRIME_DIR = '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/'



def opener():
    """
    opens the appropriate file determined by user input
    """

   # with open(, 'r') as f:
        #text = f.read()


def menu():
    """
    requests user input

    """
    options = {choice: filename for choice, filename in enumerate(os.listdir(CRIME_DIR), start=1)}
    for choice, filename in options.items():
        print(options)

    user_input = input()


menu()

