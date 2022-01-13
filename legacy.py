def substitution_cipher():
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

import random

import caesar_cipher, vinegar_cipher, substitution_cipher, cipher_functions

# decrypt an unknown text by a string
def cipher_master_unknown(text):
    if cipher_functions.is_vinegar(text):
        return vinegar_cipher.decrypt_unknown(text)
    elif cipher_functions.is_caesar(text):
        return caesar_cipher.decrypt_unknown(text)
    return substitution_cipher.decrypt_unknown(text)

# decrypt or encrypt a message helper function - encryption/decryption and the key
def decision(cipher_name):
    while True:
        method = input('(e)ncrypt or (d)ecrypt?')
        if method == 'e' or method == 'd':
            key = cipher_name.get_key()
            return method, key

# check if file exists helper funciton
def open_text_file():
    while True:
        try:
            file_name = input('What file would You like to add?')
            open(file_name, 'r')
            break
        except:
            print('no file')
    # print(f.read())
    return file_name

# decide whether you want to create a new file or simply overwrite the old one
def make_new_file():
    while True:
        new_file = input('Would you like to make a (n)ew file or overwtire the (o)ld one?')
        if new_file == 'n':
            return True
        elif new_file == 'o':
            return False

# what type of cipher to use
def cipher_type():
    while True:
        cipher = input('Would you like to use the (c)aesar, (s)ubstitution, or (v)inegar cipher')
        if cipher == 'c':
            return caesar_cipher
        elif cipher == 's':
            return substitution_cipher
        elif cipher == 'v':
            return vinegar_cipher

def master_cipher(cipher_name, method, key, file_name, new_file):
    with open(file_name) as start_file:
        file_content = start_file.read()
    if new_file:
        file_name = file_name[:file_name.rfind('.')] + '_new' + '.txt'
    if not cipher_name and key == 'u':
        text = cipher_master_unknown(file_content)
    elif method == 'e':
        text = cipher_name.encrypt(file_content, key)
    elif method == 'd':
        if key == 'u':
            text = cipher_name.decrypt_unknown(file_content)
        else:
            text = cipher_name.decrypt(file_content, key)
    with open(file_name, 'w') as end_file:
        end_file.write(text)

# cipher metod can be changed to be a user input, same for the following functions

# substitution_cipher/caesar_cipher/vinegar_cipher/False
# cipher_name = cipher_type()
# cipher_name = vinegar_cipher
cipher_name = False

# e/d
# method, key = decision(cipher_name)
method = 'd'

# u/1-26 for caesar/word for vinegar/alpahbet variation for substitution
# key = random.randint(1, 26)
# key = 'injvdmtcswkgpbarlfyhuoxeqz'
key = 'u'
# key = 'siddhartha'

# check if file exists in directory and name in string format
# file_name = open_text_file()
file_name = '../texts/beemovie_plain_new.txt'

# True/False
# do you want to make this into a new file or change original
# new_file = make_new_file()
new_file = False

if __name__ == '__main__':
    master_cipher(cipher_name, method, key, file_name, new_file)