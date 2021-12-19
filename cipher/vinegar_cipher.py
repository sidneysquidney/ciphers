import random

import cipher_functions

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_number = {letter: i for i, letter in enumerate(alphabet)}

def get_key():
    while True:
        key = input('Please specify the key - a random word, select a (r)andom key generated for you, or select (u)nkown')
        key = input('>')
        if key == 'u':
            return 'u'
        elif key == 'r':
            key = ''.join(random.choices(alphabet, k=5))
            print('Your key is:')
            print(key)
            return key
        else:
            for i in range(len(key)):
                if key[i] not in alphabet:
                    break
                elif i == len(key) - 1:
                    return key

def encrypt(text, key):
    key_numbers = [alphabet.index(l) for l in key]
    code = ''
    count = 0
    for letter in text.lower():
        if letter not in alphabet:
            code += letter
        else:
            code += alphabet[(letter_to_number[letter] + key_numbers[count]) % 26]
            count = (count + 1) % len(key)      
    return code

def decrypt(text, key):
    key_numbers = [alphabet.index(l) for l in key]
    code = ''
    count = 0
    for letter in text.lower():
        if letter not in alphabet:
            code += letter
        else:
            code += alphabet[(letter_to_number[letter] - key_numbers[count]) % 26]
            count = (count + 1) % len(key)      
    return code

def decrypt_unknown(string, get_key = False):
    ioc_list = cipher_functions.find_ioc(string)
    first_time = True
    while True:
        ioc = ioc_list.pop(0)[0]
        strings = [string[x::ioc] for x in range(ioc)]
        key = ''.join([alphabet[letter_to_number[cipher_functions.find_ngrams(string, 1, percentage = False, zeroes = True)[0][0]] - 4] for string in strings])
        if first_time:
            print(decrypt(string, key)[:200])
            satisfied = input('is this (r)ight or (w)rong')
            if satisfied == 'r':
                break
        key =  cipher_functions.vinegar_hillclimb_score(string, key)
        first_time = False
        print(decrypt(string, key))
        satisfied = input('is this (r)ight or (w)rong')
        if satisfied == 'r':
            break
    if get_key:
        return decrypt(string, key), key
    return decrypt(string, key)
 
def vinegar_cipher():
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    answer = input('>')
    while True:
        if answer == 'e':
            print('Please enter the code you want encrypted')
            text = input('>')
            print('Please enter the key')
            key = input('>')
            print(encrypt(text, key))
        elif answer == 'd':
            print('Please enter the code you want decrypted')
            text = input('>')
            print('Please enter the key')
            key = input('>')
            print(decrypt(text, key))
        
        break

if __name__ == '__main__':
    vinegar_cipher()