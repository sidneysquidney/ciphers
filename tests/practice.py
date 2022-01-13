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

print(cipher_functions.vinegar_score('advert', vbee2))
print(cipher_functions.substitution_score(skey, sbee2))
# print(cipher_functions.vinegar_score('adverx', vbee2))
# print(cipher_functions.vinegar_score('adverx', vbee2))

# print(cipher_functions.score())
print('score', cipher_functions.score(cipher_functions.find_ngrams(bee2, 2, dic = False)) == -205647.0929809534)

print('vinegar_score', cipher_functions.vinegar_score('advert', vbee2) == -205647.0929809534)
print('substitution_score', cipher_functions.substitution_score(skey, vbee2) == -205647.0929809534)

print('vinegar_get_neighbours', cipher_functions.vinegar_get_neighbours('abc') == ['abc', 'bbc', 'cbc', 'dbc', 'ebc', 'fbc', 'gbc', 'hbc', 'ibc', 'jbc', 'kbc', 'lbc', 'mbc', 'nbc', 'obc', 'pbc', 'qbc', 'rbc', 'sbc', 'tbc', 'ubc', 'vbc', 'wbc', 'xbc', 'ybc', 'zbc', 'aac', 'abc', 'acc', 'adc', 'aec', 'afc', 'agc', 'ahc', 'aic', 'ajc', 'akc', 'alc', 'amc', 'anc', 'aoc', 'apc', 'aqc', 'arc', 'asc', 'atc', 'auc', 'avc', 'awc', 'axc', 'ayc', 'azc', 'aba', 'abb', 'abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl', 'abm', 'abn', 'abo', 'abp', 'abq', 'abr', 'abs', 'abt', 'abu', 'abv', 'abw', 'abx', 'aby', 'abz'])
print('substitution_get_neighbours', cipher_functions.substitution_get_neighbours('abcdefghijklmnopqrstuvwxyz')[:3] == ['bacdefghijklmnopqrstuvwxyz','cbadefghijklmnopqrstuvwxyz','dbcaefghijklmnopqrstuvwxyz'])

print('hillclimb_master - vinegar', cipher_functions.hillclimb_master('iop', cipher_functions.vinegar_score, cipher_functions.vinegar_get_neighbours, score_arg=vbee2[:100], iterations=7) == 'key')

print('hillclimb_master - substitution', cipher_functions.hillclimb_master(alphabet, cipher_functions.substitution_score, cipher_functions.substitution_get_neighbours, score_arg=sbee2[:1000], iterations=25))
