import random

import caesar_cypher, vinegar_cypher, substitution_cypher

# decrypt or encrypt a message helper function - encryption/decryption and the key
def decision(cypher_name):
    while True:
        method = input('(e)ncrypt or (d)ecrypt?')
        if method == 'e' or method == 'd':
            key = cypher_name.get_key()
            return method, key

# check if file exists helper funciton
def open_text_file():
    while True:
        try:
            file_name = input('What file would You like to add?')
            f = open(file_name, 'r')
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
            break
        elif new_file == 'o':
            return False
            break

# what type of cypher to use
def cypher_type():
    while True:
        cypher = input('Would you like to use the (c)aesar, (s)ubstitution, or (v)inegar cypher')
        if cypher == 'c':
            return caesar_cypher
        elif cypher == 's':
            return substitution_cypher
        elif cypher == 'v':
            return vinegar_cypher

def master_cypher(cypher_name, method, key, file_name, new_file):
    if method == 'e':
        with open(file_name) as unencrypted_file:
            file_content = unencrypted_file.read()
            encrypted_message = cypher_name.encrypt(file_content, key)
        if new_file:
            file_name = file_name[:file_name.find('.')] + '_encrypted' + '.txt'
        with open(file_name, 'w') as encrypted_file:
            encrypted_file.write(encrypted_message)
    elif method == 'd':
        with open(file_name) as encrypted_file:
            file_content = encrypted_file.read()
            if key == 'unknown':
                decrypted_message = cypher_name.decrypt_unknown(file_name)
            else:
                decrypted_message = cypher_name.decrypt(file_content, key)
        if new_file:
            file_name = file_name[:file_name.find('.')] + '_decrypted' + '.txt'
        with open(file_name, 'w') as decrypted_file:
            decrypted_file.write(decrypted_message)

# cypher metod can be changed to be a user input, same for the following functions
# cypher_name = cypher_type()
cypher_name = caesar_cypher

# encrypt/decrypt and key/unknown
# method, key = decision(cypher_name)
method = 'e'
key = random.randint(1, 26)
# key = 'unknown'

# check if file exists in directory and name in string format
# file_name = open_text_file()
file_name = 's.txt'

# do you want to make this into a new file or change original
# new_file = make_new_file()
new_file = False

if __name__ == '__main__':
    master_cypher(cypher_name, method, key, file_name, new_file)

# decrypt next level, crack code without the key - done for caesar