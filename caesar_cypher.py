
import random

import words_import

most_common = words_import.most_common_words
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

# simple decryption method

# def decrypt_unknown(text):
#     for number in range(26):
#         code = ''
#         for letter in text.lower():
#             if letter not in alphabet:
#                 code += letter
#             else:
#                 code += alphabet[(letter_to_number[letter] - number) % 26]
#         print(f'{number}: ' + code)
#     while True:
#         key = input('What was the correct decryption key?')
#         if key.isdigit() and 0 <= int(key) <= 26:
#             break
#     return decrypt(text, int(key))

# coule have method to get file name in future..

def decrypt_unknown(file_name):
    with open(file_name) as file:
        content = file.read()
    c = content.split(' ')
    versions = list(range(1, 26))
    matches = {n: 0 for n in range(1, 26)}
    # print(content)
    for v in versions:
        count = 0
        for word in c:
            if decrypt(word, v) in most_common:
                count += 1
        matches[v] = count
    while True:
        highest_matches = sorted(matches.keys(), key=lambda x:matches[x]).pop()
        decrypted_content = decrypt(content, highest_matches)
        # add user input code to determine if key was correct and break loop
        break
    return decrypted_content

def caesar_cypher():
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
    caesar_cypher()