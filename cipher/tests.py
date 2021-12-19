import cipher_functions, substitution_cipher, vinegar_cipher, caesar_cipher

ciphertext = '''\
UXLIRNXSOPQAKJBJTXSVTJKRHXKKJKLIQQOEBLXRSNJKWQKQKYSAQKLRVQNLJKQD\
QRPLJRSEWIRSWQWJHQKTRKKQRWIXSODXNXJSNJTLIQBRNLLIXNXNUIRLXYSAQKLR\
VQLJAJTJKEJYKQRAQK\
'''
# turn_into_string
bee1 = cipher_functions.turn_into_string('../texts/beemovie.txt')
bee2 = cipher_functions.turn_into_string('../texts/beemovie_plain.txt')
print('turn_into_string' ,bee1[:9] == 'according')

correct_ciphertext = 'withasingledropofinkforamirrortheegyptiansorcererundertakestorevealtoanychancecomerfarreachingvisionsofthepastthisiswhatiundertaketodoforyoureader'
cbee2 = caesar_cipher.encrypt(bee2, 7)
vbee2 = vinegar_cipher.encrypt(bee2, 'key')
sbee2 = substitution_cipher.encrypt(bee2, 'injvdmtcswkgpbarlfyhuoxeqz')

# caesar_cipher.py
print('caesar_cipher.encrypt', caesar_cipher.encrypt('abcdefg', 3) == 'defghij')
print('caesar_cipher.decrypt', caesar_cipher.decrypt('defghij', 3) == 'abcdefg')
print('caesar_cipher.decrypt_unknown', caesar_cipher.decrypt_unknown(cbee2, get_key=True)[1] == 7)

# vinegar_cipher.py
print('vinegar_cipher.encrypt', vinegar_cipher.encrypt('sidiscool', 'key') == 'cmbswaysj')
print('vinegar_cipher.decrypt', vinegar_cipher.decrypt('psexegzcdwjtkp', 'work') == 'tennisishisjob')
# print('vinegar_cipher.decrypt_unknown', vinegar_cipher.decrypt_unkown(vbee2, get_key=True)[1] == 'key')

# substitution_cipher.py
print('substitution_cipher.encrypt', substitution_cipher.encrypt('noonewilleverknowthecode', 'ocbdefghijklmnapqrstuvwxyz') == 'naanewilleverknawthebade')
print('substitution_cipher.decrypt', substitution_cipher.decrypt('naanewilleverknawthebade', 'ocbdefghijklmnapqrstuvwxyz') == 'noonewilleverknowthecode')
# print('substitution_cipher.decrypt_unknown', substitution_cipher.decrypt_unknown(ciphertext, get_key=True)[0] == correct_ciphertext)

# turn_to_list
bee1_list = cipher_functions.turn_to_list(bee1)
print('turn_to_list' ,bee1_list[1] == 'to')

# common_words
print('common_words', cipher_functions.common_words[2] == 'and')

# read_bigrams
print('read_bigrams and bigrams', cipher_functions.bigrams['he'] == -3.7599265883973865)

# monograms
print('monograms', cipher_functions.monograms['E'] == 12.0)

# MinHeapString
heap = cipher_functions.MinHeapString()
print('MinHeapString class', heap.heap_limit == 10)

# permutations1
permute_test = cipher_functions.Permutations()
print('Permutations class', permute_test.permute([l for l in 'abc']) == [['a', 'b', 'c'], ['a', 'c', 'b'],['b', 'a', 'c'],
                                                   ['b', 'c', 'a'],['c', 'a', 'b'], ['c', 'b', 'a']])

# permutations2
permute_test2 = cipher_functions.Permutations2(n = 2)
print('Permutaions2 class', permute_test2.permute([l for l in 'abc']) == [['a', 'a'], ['a', 'b'], ['a', 'c'], 
                                                    ['b', 'a'], ['b', 'b'], ['b', 'c'], 
                                                    ['c', 'a'], ['c', 'b'], ['c', 'c']])

# create_dictionary
dictionary_test = cipher_functions.create_dictionary(2)
print('create_dictionary', dictionary_test['bb'] == 0)

# find_ngrams
print('find_ngrams', cipher_functions.find_ngrams(bee1, 2)[0][0] == 'th')

# score
print('score', cipher_functions.score(cipher_functions.find_ngrams(ciphertext, 2, dic = False)) == -1380.9684879021993)

# swap
print('swap', cipher_functions.swap('sidney', 1, 2) == 'sdiney')

# hillclimb_key
print('hillclimb_key', cipher_functions.hillclimb_key(ciphertext)[0] == 'j')

# hillclimb_score
print('hillclimb_score', cipher_functions.hillclimb_score(ciphertext) == 'rvwaqboixmctdsjpgknlyhufez')

# letters_to_keys
print('letters_to_keys', cipher_functions.letters_to_keys('vm', 'rcwaqtoixmvpdsjbgknlyhufez')
      == ['rcwaqtoixmvpdsjbgknlyhufez', 'rcwaqtoixvmpdsjbgknlyhufez'])

# vinegar_hillclimb_score
print('vinegar_hillclimb_score', cipher_functions.vinegar_hillclimb_score(vbee2[:100], 'asz') == 'key')

# ioc_score
print('ioc_score', cipher_functions.ioc_score(cipher_functions.find_ngrams(bee2, 1, percentage = False, zeroes = True)) == 1.6562549441687844)

# find_ioc
print('find_ioc', cipher_functions.find_ioc(vbee2)[0][0] == 3)

# caesar_list
print('caesar_list', [x[0] for x in cipher_functions.caesar_list(cbee2[:100])][:5] == [7, 13, 3, 26, 18])

# is_caesar
print('is_caesar', [cipher_functions.is_caesar(cbee2), cipher_functions.is_caesar(vbee2), cipher_functions.is_caesar(sbee2)] == [True, False, False])

# is_vinegar
print('is_vinegar', [cipher_functions.is_vinegar(vbee2), cipher_functions.is_vinegar(cbee2), cipher_functions.is_vinegar(sbee2)] == [True, False, False])

# # vinegar_decipher
# print('vinegar_decipher', cipher_functions.vinegar_decipher(vbee2) == 'key')

# # dictionary_attack5
# print('dictionary_attack5', cipher_functions.dictionary_attack5(substitution_cipher.decrypt(ciphertext, 'rcwaqboixzvpdsjtgknlyhufem')) == 'abcdepghijklvnofqrstumwxyz')

# # substitution_decipher
# print('substitution_decipher', cipher_functions.substitution_decipher(ciphertext) == correct_ciphertext)

