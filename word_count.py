import re
from collections import Counter

BOOK ='geneology_of_morals.txt'
def get_data(book_filepath):
    """
    File handler function, opens the file
    and returns the contents as a single string.
    """

    with open (BOOK, 'r') as file:
        text = file.read()
        return text


def clean_text(not_clean_data):
    """
    Cleans the data of noise
    Make all text lowercase and remove some extensions
    """
    raw_text = get_data(BOOK).strip()
    cleaned_data = re.sub(r'[^a-zA-Z\s]', '', not_clean_data).replace('\n', ' ')
    return cleaned_data


def process_text(clean_text):
    """
    splits clean text data into a list
    """
    words = clean_text.split()
    wordset = {}

    for word in words:
        wordset[word] = wordset.get(word, 0) + 1
        print(word)
    return wordset


def display_results(wordset):
    """
    Prints a beautiful output of the results
    """
    print(wordset)


def one_to_rule_them_all():
    """
    Do all the things
    """
    raw_data = get_data(BOOK)
    cleaned_data = clean_text(raw_data)
    wordset = process_text(cleaned_data)
    display_results(wordset)

if __name__ == "__main__":
    one_to_rule_them_all()
