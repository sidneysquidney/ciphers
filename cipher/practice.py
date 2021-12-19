import random

import cipher_functions, substitution_cipher, vinegar_cipher, caesar_cipher, cipher_master

ciphertext = '''\
UXLIRNXSOPQAKJBJTXSVTJKRHXKKJKLIQQOEBLXRSNJKWQKQKYSAQKLRVQNLJKQD\
QRPLJRSEWIRSWQWJHQKTRKKQRWIXSODXNXJSNJTLIQBRNLLIXNXNUIRLXYSAQKLR\
VQLJAJTJKEJYKQRAQK\
'''
correct_ciphertext = 'withasingledropofinkforamirrortheegyptiansorcererundertakestorevealtoanychancecomerfarreachingvisionsofthepastthisiswhatiundertaketodoforyoureader'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_number = {letter: i for i, letter in enumerate(alphabet)}

alphabet2 = [l for l in 'abcdefghijklmnopqrstuvwxyz']
random.shuffle(alphabet2)
skey = ''.join(alphabet2)


# turn_into_string
bee1 = cipher_functions.turn_into_string('../texts/beemovie.txt')
bee2 = cipher_functions.turn_into_string('../texts/beemovie_plain.txt')

vbee2 = vinegar_cipher.encrypt(bee2, 'advert')
cbee2 = caesar_cipher.encrypt(bee2, 7)
sbee2 = substitution_cipher.encrypt(bee2, skey)

vciphertext = vinegar_cipher.encrypt(correct_ciphertext, 'key')
cciphertext = caesar_cipher.encrypt(correct_ciphertext, 10)
sciphertext = substitution_cipher.encrypt(correct_ciphertext, skey)

# second stage of decryption. take mostly completed text, instead of fixing the key, start a new key to alter
# takes user input and asks which letters are in the wrong places. then switches all around

def dictionary_attack5(text):
    print(text)
    incorrect = input('what are the wrong letters?')
    keys = cipher_functions.letters_to_keys(incorrect, alphabet)
    keys_count = []
    for i in range(len(keys)):
        decrypted_text = substitution_cipher.encrypt(text, keys[i])
        # print(decrypted_text)
        count = len([word for word in cipher_functions.common_words if word in decrypted_text])
        keys_count.append([keys[i], count])
#         print(i, keys[i], count, decrypted_text == correct_ciphertext)
    keys_count = sorted(keys_count, key=lambda x:x[1], reverse = True)
    while True:
        key = keys_count.pop(0)[0]
        print(substitution_cipher.encrypt(text, key))
        satisfied = input('is this (r)ight or (w)rong')
        if satisfied == 'r':
            break
    return key


# wrong_letters = fpvm
# print(dictionary_attack5(substitution_cipher.decrypt(ciphertext, 'rcwaqboixzvpdsjtgknlyhufem')) == 'abcdepghijklvnofqrstumwxyz')

# print([x[0] for x in cipher_functions.caesar_list(cbee2[:100])][:5])
# print('y')
# print(cipher_functions.is_vinegar(cciphertext[:1000]))
# print(cipher_functions.is_vinegar(sciphertext[:1000]))
# print(cipher_functions.is_vinegar(vciphertext[:1000]))

# print(cipher_functions.is_vinegar(cbee2))
# print(cipher_functions.is_vinegar(vbee2))
# print(cipher_functions.is_vinegar(sbee2))


# print(cipher_master_text.cipher_master2(sbee2))

