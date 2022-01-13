# import external packages first. Doesn't matter for the code but is advised practice for readability
import numpy as np

# don't use relative import like: from cipher_functions import create_ngrams_dict, ALPHABET
# import from the whole package, prevents importing things twice
from cipher.cipher_functions import create_ngrams_dict, ALPHABET

def score(list_of_bigrams, bigrams):
    # score function that takes in a list of bigrams and sums the values from the bigrams dictionary
    lst = [[x, bigrams[x]] for x in list_of_bigrams]
    return sum([x[1] for x in lst])

def score_ngrams(key, text, bigrams, ciphertype):
    return score(find_ngrams(ciphertype.decrypt(text, key), 2, dic = False), bigrams)

def find_ngrams(text, letter_count, dic = True, percentage = True, ordered = True, log = True, zeroes = False):
    """function to take an encryption, count the letters/pairs - by letter count
    (eg letter count = 1 -> a,b,c,d,e,f,g, letter count = 2 -> ab, ac, ad, ee, gr, th...)
    parameters include dic/list, percentage, ordered, log"""
    text = ''.join([l for l in text.lower() if l in ALPHABET])
    number_ngrams = len(text) - letter_count + 1
    ngrams = [None for g in range(number_ngrams)]
    for i in range(len(ngrams)):
        ngrams[i] = text[i: i + letter_count]  
    if dic:
        ngrams_count = create_ngrams_dict(letter_count)
        for g in ngrams:
            ngrams_count[g] += 1
        if percentage:
            for key in ngrams_count.keys():
                ngrams_count[key] /= number_ngrams 
                if log:
                    if ngrams_count[key] == 0:
                        continue
                    ngrams_count[key] = np.log(ngrams_count[key])
        if ordered:
            ngrams_count = sorted(ngrams_count.items(), key=lambda x:x[1], reverse = True)
        if not zeroes:
            ngrams_count = [x for x in ngrams_count if x[1] != 0]
        return ngrams_count
    return ngrams


def ioc_score(lst):
    """takes a list of tuples with the letters first index and their frequency second index, then performs the ioc sum
    eg [('k', 17),('q', 17),('j', 14)... ]"""
    length = sum([x[1] for x in lst])
    scores = [(x[1] / length) * ((x[1] - 1)  / (length - 1)) for x in lst]
    total = 26 * sum(scores)
    return total


def find_ioc(string):
    # finds the index of coincidence for each number of letters up to 26 to determine if a vinegar cipher. 
    # Returns: list of tuples in order of the most likely index of coincidence (eg 'key' = 3)
    dct = {n: [string[x::n] for x in range(5)] for n in range(1, 27)}
    dct2 = {n: None for n in range(1, 27)}
    for n in range(1, 27):
        ngrams = [find_ngrams(dct[n][x], 1, percentage = False, zeroes = True) for x in range(5)]
        scores = [ioc_score(x) for x in ngrams]
        dct2[n] = sum(scores) / len(scores)
    score_list = sorted(list(dct2.items()), key=lambda x:abs(x[1] - 1.7), reverse = False)
    temp_list = score_list
    score_list = [score for score in score_list if abs(score_list[0][1] - score[1]) <= 0.1]
    score_list = sorted(score_list) + [x for x in temp_list if x not in score_list]
    return score_list