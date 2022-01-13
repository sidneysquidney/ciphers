import numpy as np

from cipher import ALPHABET, LETTER_TO_NUMBER, cipher_functions
from cipher.freq_analysis import find_ioc, find_ngrams, score, score_ngrams
from cipher.ciphertypes import caesar, vinegar, substitution
from cipher.hillclimb import hillclimb


def is_vinegar(string):
    #lst = np.array(sorted([x[1] for x in find_ioc(string)]))
    #if np.std(lst) > 0.1:
    #    return True
    #return False
    return any(x[1] > 1.5 for x in find_ioc(string)[1:])

def is_caesar(string, bigrams):
    lst = caesar_list(string, bigrams)
    lst = np.array([x[1] for x in lst])
    q1, q3 = np.percentile(lst, [10, 90])
    iqr = abs(q1 - q3)
    upper = q3 + iqr
    if lst[0] > upper:
        return True
    return False

def vinegar_decipher(text, bigrams):
    ioc_list = find_ioc(text)
    first_time = True
    while True:
        ioc = ioc_list.pop(0)[0]
        texts = [text[x::ioc] for x in range(ioc)]
        key = ''.join([ALPHABET[LETTER_TO_NUMBER[find_ngrams(text, 1, percentage = False, zeroes = True)[0][0]] - 4] for text in texts])
        if first_time:
            decrypted_text = vinegar.decrypt(text, key)
            print(decrypted_text)
            satisfied = input('is this (r)ight or (w)rong')
            if satisfied == 'r':
                break
        key = hillclimb(key, score_ngrams, vinegar.get_neighbours, score_args=(text, bigrams, vinegar))
        first_time = False
        decrypted_text = vinegar.decrypt(text, key)
        print(decrypted_text)
        satisfied = input('is this (r)ight or (w)rong')
        if satisfied == 'r':
            break
    return decrypted_text, key

def caesar_list(text, bigrams):
    text = ''.join([x for x in text if x in ALPHABET])
    versions = {n: caesar.decrypt(text, n) for n in range(1, 27)}
    versions_scores = {n: None for n in range(1, 27)}
    for n in range(1, 27):
        versions_scores[n] = score(find_ngrams(versions[n], 2, dic = False), bigrams)
    return sorted(versions_scores.items(), key=lambda x:x[1], reverse = True)


def caesar_decipher(text, bigrams, get_key = False):
    # caesar cipher decrypt unknown decrypts using bigram score.
    versions_scores = caesar_list(text, bigrams)
    if get_key:
        return caesar.decrypt(text, versions_scores[0][0]), versions_scores[0][0]
    return caesar.decrypt(text, versions_scores[0][0])


def substitution_decipher(text, monograms, bigrams, common_words, get_keys = False):
    key = start_key(text, monograms)
    key1 = hillclimb(key, score_ngrams, substitution.get_neighbours, score_args=(text, bigrams, substitution))
    text2 = substitution.decrypt(text, key1)
    key2 = dictionary_attack5(text2, common_words)
    if get_keys:
        return substitution.double_key_combo(text, key1, key2), [key1, key2]
    return substitution.double_key_combo(text, key1, key2)

def dictionary_attack5(text, common_words):
    # second stage of decryption. take mostly completed text, instead of fixing the key, start a new key to alter
    # takes user input and asks which letters are in the wrong places. then switches all around
    text = text[:200]
    print(text)
    incorrect = input('what are the wrong letters?')
    keys = cipher_functions.letters_to_keys(incorrect, ALPHABET)
    keys_count = []
    for i in range(len(keys)):
        decrypted_text = substitution.encrypt(text, keys[i])
        count = len([word for word in common_words if word in decrypted_text])
        keys_count.append([keys[i], count])
        # print(i, keys[i], count, decrypted_text == correct_ciphertext)
    keys_count = sorted(keys_count, key=lambda x:x[1], reverse = True)
    while True:
        key = keys_count.pop(0)[0]
        print(substitution.encrypt(text, key))
        satisfied = input('is this (r)ight or (w)rong')
        if satisfied == 'r':
            break
    return key

def start_key(encrypted_text, monograms: list):
    # get start key for the hill climb from the list of monograms in the encyrypted text
    frequency = find_ngrams(encrypted_text, 1, zeroes = True, log = False)
    start_key = ''
    for l in ALPHABET:
        i = monograms.index(l)
        start_key += frequency[i][0]
    return start_key