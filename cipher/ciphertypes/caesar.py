import random

from cipher import ALPHABET, LETTER_TO_NUMBER

def get_key():
    while True:
        key = input('Please specify the key - a number between 1 and 26, select a (r)andom key generated for you, or select (u)nkown')
        if key == 'r':
            key = random.randint(1, 26)
            return key
        elif key == 'u':
            return 'unknown'
        elif key.isdigit() and 0 <= int(key) <= 26:
            return int(key)


def encrypt(text, number):
    code = ''
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += ALPHABET[(LETTER_TO_NUMBER[letter] + number) % 26]
    return code


def decrypt(text, number):
    code = ''
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += ALPHABET[(LETTER_TO_NUMBER[letter] - number) % 26]
    return code