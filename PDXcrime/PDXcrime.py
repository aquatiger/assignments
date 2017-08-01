"""
Offers various summations of crime data from Portland, Oregon during the years 2011-2014
Gives user options for the most and least of any option, like zip code or year

"""
from collections import Counter
import os


CRIME_DIR = '/home/roger/Git/PythonFullStack/1_Python/3_Applied_Python/labs/pdx_crime_data/data/'



def opener(path):
    """
    opens the appropriate file determined by user input
    """
     with open(CRIME_DIR+path, 'r') as f:
         text = f.read()
         return text


def splitter(text):
    """
    splits data from a string to a list
    :param text: text from opener function
    :return: data that has been split according to each row
    """

def sorter(split_data):
    """

    :param split_data: data from splitter function
    :return: sorted data
    """

def counter(dataset) :
    """
    :param dataset:
    :return:
    """
    crimes = [crime[3] for crime in dataset]
    c = Counter


def filter(dataset, query):
    """
    counts the number of instances of each category
    :return:
    """
    result = len([crime for crime in dataset if query in crime])
    return result

def menu():
    """
    requests user input

    """
    options = {choice: filename for choice, filename in enumerate(os.listdir(CRIME_DIR), start=1)}
    for choice, filename in options.items():
        print(options)

    user_input = input()


