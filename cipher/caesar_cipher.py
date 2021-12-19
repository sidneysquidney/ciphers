import random

import cipher_functions

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_number = {letter: i for i, letter in enumerate(alphabet)}

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
        if letter not in alphabet:
            code += letter
        else:
            code += alphabet[(letter_to_number[letter] + number) % 26]
    return code

def decrypt(text, number):
    code = ''
    for letter in text.lower():
        if letter not in alphabet:
            code += letter
        else:
            code += alphabet[(letter_to_number[letter] - number) % 26]
    return code

# caesar cipher decrypt unknown decrypts using bigram score.

def decrypt_unknown(text, get_key = False):
    text = ''.join([x for x in text if x in alphabet])
    versions = {n: decrypt(text, n) for n in range(1, 27)}
    versions_scores = {n: None for n in range(1, 27)}
    for n in range(1, 27):
        versions_scores[n] = cipher_functions.score(cipher_functions.find_ngrams(versions[n], 2, dic = False))
    versions_scores = sorted(versions_scores.items(), key=lambda x:x[1], reverse = True)
    if get_key:
        return decrypt(text, versions_scores[0][0]), versions_scores[0][0]
    return decrypt(text, versions_scores[0][0])

def caesar_cipher():
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        answer = input('>')
        if answer == 'e' or answer == 'd':
            while True:
                print('Please enter a key (0 - 26) to use.')
                key = input('>')
                if key.isdigit() and 0 <= int(key) <= 26:
                    if answer == 'e':
                        print('Please enter the code you want encrypted')
                        text = input('>')
                        print(encrypt(text, int(key)))
                    else:
                        print('Please enter the code you want decrypted')
                        text = input('>')
                        print(decrypt(text, int(key)))
                    break
            break
      
if __name__ == '__main__':
    caesar_cipher()