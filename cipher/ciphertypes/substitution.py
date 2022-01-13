import random
import numpy as np

from cipher import ALPHABET
from cipher.cipher_functions import swap

# helper function to take text with 2 keys to decrypt, then encrypt, and therefore decrypt overall
def double_key_combo(text, key1, key2):
    return encrypt(decrypt(text, key1), key2)


def get_neighbours(key):
    neighbours = list(np.zeros(shape=325))
    i = 0
    for i1 in range(26):
        for i2 in range(i1 + 1, 26):
            neighbours[i] = swap(key, i1, i2)
            i += 1
    return neighbours


def get_key():
    ALPHABET2 = [l for l in 'abcdefghijklmnopqrstuvwxyz']
    while True:
        key = input('Please specify the key - ALPHABET in a unique order, select a (r)andom key generated for you, or select (u)nkown')
        if key == 'r':
            random.shuffle(ALPHABET2)
            print('Your key is:')
            print(''.join(ALPHABET2))
            return ''.join(ALPHABET2)
        elif key == 'u':
            return 'unknown'
        elif len(key) == 26:
            for l in ALPHABET:
                if l not in key.lower():
                    break
                if l == 'z':
                    return key.lower()

def encrypt(text, key):
    code = ''
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += key[ALPHABET.index(letter)]
    return code

def decrypt(text, key):
    code = ''
    for letter in text.lower():
        if letter not in ALPHABET:
            code += letter
        else:
            code += ALPHABET[key.index(letter)]
    return code