import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_number = {letter: i for i, letter in enumerate(alphabet)}

def get_key():
    while True:
        key = input('Please specify the key - a random word, select a (r)andom key generated for you, or select (u)nkown')
        key = input('>')
        if key == 'u':
            return 'unknwon'
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
 
def vinegar_cypher():
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
    vinegar_cypher()