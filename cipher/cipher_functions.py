
#from cipher.freq_analysis import find_ngrams
from cipher import ALPHABET
from cipher.permutations import Permutations, Permutations2


# returns a list of words from a string when the string is seperated by spaces. 
def turn_to_list(string):
    return [x.strip('.,!?') for x in string.split(' ') if x != '' or x not in ALPHABET]

def create_ngrams_dict(n):
    # create a dictionary of all the grams of n length, going to 0
    keys = Permutations2(n)
    keys.permute(ALPHABET)
    dictionary = {''.join(x): 0 for x in keys.result}
    return dictionary

def letters_to_keys(letters, key):
    # takes in letters, returns a list of all the possible keys made by mixing those letters within the key
    key_indicies = [key.index(l) for l in letters]
    index_permutations = Permutations()
    index_permutations.permute(key_indicies)
    keys = []
    for lst in index_permutations.result:
        key = list(key)
        for i in range(len(lst)):
            key[lst[i]] = letters[i]
        keys.append(''.join(key))
    return keys

def swap(string, index1, index2):
    # return a string swapping letter at index1 with letter at index2
    if index1 == index2:
        return string
    index1, index2 = min(index1, index2), max(index1, index2)
    return string[:index1] + string[index2] + string[index1 + 1:index2] + string[index1] + string[index2 + 1:]
