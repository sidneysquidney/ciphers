import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def get_key():
    alphabet2 = [l for l in 'abcdefghijklmnopqrstuvwxyz']
    while True:
        key = input('Please specify the key - alphabet in a unique order, select a (r)andom key generated for you, or select (u)nkown')
        if key == 'r':
            random.shuffle(alphabet2)
            print('Your key is:')
            print(''.join(alphabet2))
            return ''.join(alphabet2)
        elif key == 'u':
            return 'unknown'
        elif len(key) == 26:
            for l in alphabet:
                if l not in key.lower():
                    break
                if l == 'z':
                    return key.lower()

def encrypt(text, key):
    code = ''
    for letter in text.lower():
        if letter not in alphabet:
            code += letter
        else:
            code += key[alphabet.index(letter)]
    return code

def decrypt(text, key):
    code = ''
    for letter in text.lower():
        if letter not in alphabet:
            code += letter
        else:
            code += alphabet[key.index(letter)]
    return code

def substitution_cypher():
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    answer = input('>')
    while True:
        if answer == 'e':
            print('Please enter the code you want encrypted')
            text = input('>')
            key = get_key()
            print('If you would like to save the key for future decryptions:')
            print(key)
            print(encrypt(text, key))
        elif answer == 'd':
            print('Please enter the code you want decrypted')
            text = input('>')
            print('Please enter the decryption key')
            key = input('>')
            print(decrypt(text, key))
        
        break

if __name__ == '__main__':
    substitution_cypher()