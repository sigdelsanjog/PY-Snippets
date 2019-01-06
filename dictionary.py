import json
import difflib

from difflib import SequenceMatcher


data = json.load(open("dictionary.json"))


def fetch_meaning(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]


input_word = input("Enter a word: ")

print(fetch_meaning(input_word))
