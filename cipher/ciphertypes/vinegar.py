import random
import numpy as np

from cipher import ALPHABET, LETTER_TO_NUMBER

def get_neighbours(key):
    neighbours = list(np.zeros(shape=len(key) * 26))
    for i1 in range(len(key)):
        for i in range(len(ALPHABET)):
            neighbours[i1 * 26 + i] = key[:i1] + ALPHABET[i] + key[i1 + 1:]
    return neighbours


def get_key():
    while True:
        key = input('Please specify the key - a random word, select a (r)andom key generated for you, or select (u)nkown')
        key = input('>')
        if key == 'u':
            return 'u'
        elif key == 'r':
            key = ''.join(random.choices(ALPHABET, k=5))
            print('Your key is:')
            print(key)
            return key
        else:
            for i in range(len(key)):
                if key[i] not in ALPHABET:
                    break
                elif i == len(key) - 1:
                    return key


def encrypt(text, key):
    key_numbers = [ALPHABET.index(l) for l in key]
    code = ''
    count = 0
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += ALPHABET[(LETTER_TO_NUMBER[letter] + key_numbers[count]) % 26]
            count = (count + 1) % len(key)      
    return code


def decrypt(text, key):
    key_numbers = [ALPHABET.index(l) for l in key]
    code = ''
    count = 0
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += ALPHABET[(LETTER_TO_NUMBER[letter] - key_numbers[count]) % 26]
            count = (count + 1) % len(key)      
    return code
