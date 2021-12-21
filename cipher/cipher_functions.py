import numpy as np
import pandas as pd
import random

import vinegar_cipher, substitution_cipher, caesar_cipher

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_number = {letter: i for i, letter in enumerate(alphabet)}

# returns the string from a text file, all in lower case

def turn_into_string(file_name):
    with open(file_name, 'r') as file:
        content = file.read().replace('\n', ' ')
    return content.lower()

# returns a list of words from a string when the string is seperated by spaces. 

def turn_to_list(string):
    return [x.strip('.,!?') for x in string.split(' ') if x != '' or x not in alphabet]

common_words = turn_to_list(turn_into_string('../texts/google-10000-english-no-swears.txt'))

# returns the natural log of the percentage of each bigram from a csv file
# eg 'th' count 100, divide by total number of bigrams for percentage, find natural log.

def read_bigrams(filename):
    df = pd.read_csv(filename, delimiter=' ', names=['bigrams','count'], keep_default_na=False)
    total = sum(df['count'])
    bigrams, count = df['bigrams'], df['count'] / total
    frequency_dict = {bigrams[i].lower(): np.log(count[i]) for i in range(len(bigrams))}
    return frequency_dict

bigrams = read_bigrams('../texts/bigrams.csv')

# dictinary and list of most frequent monograms in the english language

monograms = {'E' : 12.0,'T' : 9.10,'A' : 8.12,'O' : 7.68,'I' : 7.31,'N' : 6.95,'S' : 6.28,'R' : 6.02,
'H' : 5.92,'D' : 4.32,'L' : 3.98,'U' : 2.88,'C' : 2.71,'M' : 2.61,'F' : 2.30,'Y' : 2.11,'W' : 2.09,'G' : 2.03,
'P' : 1.82,'B' : 1.49,'V' : 1.11,'K' : 0.69,'X' : 0.17,'Q' : 0.11,'J' : 0.10,'Z' : 0.07 }

monograms_list = [l.lower() for l in monograms.keys()]

# Min Heap of tuples (string, number) to help with (key, score) sorting

class MinHeapString:
    def __init__(self, heap_limit = 10):
        self.count = 0
        self.heap_list = [None]
        self.max = None
        self.heap_limit = heap_limit
        
    def left_child_idx(self, idx):
        return idx * 2
    
    def right_child_idx(self, idx):
        return idx * 2 + 1
    
    def parent_idx(self, idx):
        return idx // 2
    
    def has_children(self, idx):
        return self.left_child_idx(idx) <= self.count
    
    def smaller_child_idx(self, idx):
        if self.has_children(idx):
            if self.right_child_idx(idx) > self.count:
                return self.left_child_idx(idx)
            else:
                left = self.left_child_idx(idx)
                right = self.right_child_idx(idx)
                if self.heap_list[left][1] < self.heap_list[right][1]:
                    return left
                else:
                    return right 
                
    def add(self, value):      
        if (self.count < self.heap_limit) or (value[1] > self.heap_list[1][1]):
            self.heap_list.append(value) 
            self.count += 1
            self.heapify_up(self.count)
            if not self.max:
                self.max = value
            elif value[1] > self.max[1]:
                self.max = value
            if self.count > self.heap_limit:
                self.remove_min()
                
    def remove_min(self):
        smallest = self.heap_list[1]
        temp = self.heap_list[self.count]
        self.heap_list[1] = temp
        self.heap_list[self.count] = smallest
        self.heap_list.pop()
        self.count -= 1
        self.heapify_down()
        return smallest
    
    def heapify_up(self, idx):
        while self.parent_idx(idx) > 0:
            parent = self.parent_idx(idx)
            if self.heap_list[parent][1] > self.heap_list[idx][1]:
                temp = self.heap_list[parent]
                self.heap_list[parent] = self.heap_list[idx]
                self.heap_list[idx] = temp
            idx = self.parent_idx(idx)
            
    def heapify_down(self):
        idx = 1
        while self.has_children(idx):
            new_index = self.smaller_child_idx(idx)
            if self.heap_list[idx][1] > self.heap_list[self.smaller_child_idx(idx)][1]:
                temp = self.heap_list[idx]
                self.heap_list[idx] = self.heap_list[self.smaller_child_idx(idx)]
                self.heap_list[self.smaller_child_idx(idx)] = temp
            idx = new_index

# gets permutations from a string or list, returns all possible permutations
# eg 123 - 123,132, 231, 213, 312, 321

class Permutations:
    def __init__(self):
        self.result = []
        
    def permute(self, lst):
        self.backtrack(lst, [])
        return self.result
    
    def backtrack(self, lst, path):
        if not lst:
            self.result.append(path)
        for x in range(len(lst)):
            self.backtrack(lst[:x] + lst[x + 1:], path + [lst[x]])

# gets permutations from a string or list, returns all possible permutations of length n, repeats allowed
# eg 123, n = 2 - 11, 12, 13, 21, 22, 23, 31, 32, 33
# this is also a helper function to create a dictionary of ngrams

class Permutations2:
    def __init__(self, n = 1):
        self.result = []
        self.n = n
    def permute(self, lst):
        self.backtrack(lst, [])
        return self.result
    def backtrack(self, lst, path):
        if len(path) == self.n:
            self.result.append(path)           
        for x in range(len(lst)):
            if len(path) == self.n:
                continue
            self.backtrack(lst, path + [lst[x]])

# create a dictionary of all the grams of n length, going to 0

def create_dictionary(n):
    keys = Permutations2(n)
    keys.permute(alphabet)
    dictionary = {''.join(x): 0 for x in keys.result}
    return dictionary

# function to take an encryption, count the letters/pairs - by letter count 
# (eg letter count = 1 -> a,b,c,d,e,f,g, letter count = 2 -> ab, ac, ad, ee, gr, th...)
# parameters include dic/list, percentage, ordered, log

def find_ngrams(text, letter_count, dic = True, percentage = True, ordered = True, log = True, zeroes = False):
    text = ''.join([l for l in text.lower() if l in alphabet])
    number_ngrams = len(text) - letter_count + 1
    ngrams = [None for g in range(number_ngrams)]
    for i in range(len(ngrams)):
        ngrams[i] = text[i: i + letter_count]  
    if dic:
        ngrams_count = create_dictionary(letter_count)
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

# score function that takes in a list of bigrams and sums the values from the bigrams dictionary

def score(list_of_bigrams):
    lst = [[x, bigrams[x]] for x in list_of_bigrams]
    return sum([x[1] for x in lst])

# return a string swapping letter at index1 with letter at index2

def swap(string, index1, index2):
    if index1 == index2:
        return string
    index1, index2 = min(index1, index2), max(index1, index2)
    return string[:index1] + string[index2] + string[index1 + 1:index2] + string[index1] + string[index2 + 1:]

# get start key for the hill climb from the list of monograms in the encyrypted text

def hillclimb_key(encrypted_text):
    frequency = find_ngrams(encrypted_text, 1, zeroes = True, log = False)
    start_key = ''
    for l in alphabet:
        i = monograms_list.index(l)
        start_key += frequency[i][0]
    return start_key

# second stage of decryption. take mostly completed text, instead of fixing the key, start a new key to alter
# takes user input and asks which letters are in the wrong places. then switches all around

def dictionary_attack5(text):
    text = text[:200]
    print(text)
    incorrect = input('what are the wrong letters?')
    keys = letters_to_keys(incorrect, alphabet)
    keys_count = []
    for i in range(len(keys)):
        decrypted_text = substitution_cipher.encrypt(text, keys[i])
#         print(decrypted_text)
        count = len([word for word in common_words if word in decrypted_text])
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

# gets the bigrams count, and creates a key that matches a text that most resembles the english language. 

def hillclimb_score(encrypted_text):
    start_key = hillclimb_key(encrypted_text)
    potential_new_keys = MinHeapString()
    potential_new_keys.add([start_key, score(find_ngrams(encrypted_text, 2, dic = False))])
    count = 0
    while True:
        count += 1
        for i1 in range(len(start_key)):
            for i2 in range(len(start_key)):
                if i1 == i2:
                    continue
                key = swap(start_key, i1, i2)
                key_score = score(find_ngrams(substitution_cipher.decrypt(encrypted_text, key), 2, dic = False))
                potential_new_keys.add([key, key_score])
#         start_key = random.choice(potential_new_keys.heap_list[1:])[0]
        start_key = potential_new_keys.max[0]
        if count == 25:
            break
    return start_key

# takes in letters, returns a list of all the possible keys made by mixing those letters within the key

def letters_to_keys(letters, key):
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

# helper function to take text with 2 keys to decrypt, then encrypt, and therefore decrypt overall

def double_key_combo(text, key1, key2):
    return substitution_cipher.encrypt(substitution_cipher.decrypt(text, key1), key2)

# hillclimb for the vinegar cipher - same as previous hillclimb but swaps letters with alphabet, 
# start_key should have the right length derived from find_ioc previously 
# eg start_key should have length 3 if key = 'key'

def vinegar_hillclimb_score(encrypted_text, start_key):
    potential_new_keys = MinHeapString()
    potential_new_keys.add([start_key, score(find_ngrams(encrypted_text, 2, dic = False))])
    count = 0
    while True:
        count += 1
        for i1 in range(len(start_key)):
            for l in alphabet:
                key = start_key[:i1] + l + start_key[i1 + 1:]
                key_score = score(find_ngrams(vinegar_cipher.decrypt(encrypted_text, key), 2, dic = False))
                potential_new_keys.add([key, key_score])
        start_key = potential_new_keys.max[0]
        if count == 25:
            break
    return start_key  

# takes a list of tuples with the letters first index and their frequency second index, then performs the ioc sum
# eg [('k', 17),('q', 17),('j', 14)... ]

def ioc_score(lst):
    length = sum([x[1] for x in lst])
    scores = [(x[1] / length) * ((x[1] - 1)  / (length - 1)) for x in lst]
    total = 26 * sum(scores)
    return total

# finds the index of coincidence for each number of letters up to 26 to determine if a vinegar cipher. 
# Returns a list of tuples in order of the most likely index of coincidence (eg 'key' = 3)

def find_ioc(string):
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

def is_vinegar(string):
    lst = np.array(sorted([x[1] for x in find_ioc(string)]))
    if np.std(lst) > 0.1:
        return True
    return False

def is_caesar(string):
    lst = caesar_list(string)
    lst = np.array([x[1] for x in lst])
    q1, q3 = np.percentile(lst, [10, 90])
    iqr = abs(q1 - q3)
    upper = q3 + iqr
    if lst[0] > upper:
        return True
    return False

def caesar_list(text):
    text = ''.join([x for x in text if x in alphabet])
    versions = {n: caesar_cipher.decrypt(text, n) for n in range(1, 27)}
    versions_scores = {n: None for n in range(1, 27)}
    for n in range(1, 27):
        versions_scores[n] = score(find_ngrams(versions[n], 2, dic = False))
    return sorted(versions_scores.items(), key=lambda x:x[1], reverse = True)

def substitution_decipher(text, get_keys = False):
    key1 = hillclimb_score(text)
    text2 = substitution_cipher.decrypt(text, key1)
    key2 = dictionary_attack5(text2)
    if get_keys:
        return double_key_combo(text, key1, key2), [key1, key2]
    return double_key_combo(text, key1, key2)

def vinegar_decipher(string):
    ioc_list = find_ioc(string)
    first_time = True
    while True:
        ioc = ioc_list.pop(0)[0]
        strings = [string[x::ioc] for x in range(ioc)]
        key = ''.join([alphabet[letter_to_number[find_ngrams(string, 1, percentage = False, zeroes = True)[0][0]] - 4] for string in strings])
        if first_time:
            print(vinegar_cipher.decrypt(string, key)[:200])
            satisfied = input('is this (r)ight or (w)rong')
            if satisfied == 'r':
                break
        key = vinegar_hillclimb_score(string, key)
        first_time = False
        print(vinegar_cipher.decrypt(string, key))
        satisfied = input('is this (r)ight or (w)rong')
        if satisfied == 'r':
            break
    return key

def vinegar_score(key, text):
    return score(find_ngrams(vinegar_cipher.decrypt(text, key), 2, dic = False))

def substitution_score(key, text):
    return score(find_ngrams(substitution_cipher.decrypt(text, key), 2, dic = False))

def vinegar_get_neighbours(key):
    neighbours = list(np.zeros(shape=len(key) * 26))
    for i1 in range(len(key)):
        for i in range(len(alphabet)):
            neighbours[i1 * 26 + i] = key[:i1] + alphabet[i] + key[i1 + 1:]
    return neighbours

def substitution_get_neighbours(key):
    neighbours = list(np.zeros(shape=325))
    i = 0
    for i1 in range(26):
        for i2 in range(i1 + 1, 26):
            neighbours[i] = swap(key, i1, i2)
            i += 1
    return neighbours

def hillclimb_master(start_node, score_func, neighbours_func, score_arg=None, iterations=25):
    node = start_node
    current_score = score_func(node, score_arg)
    count = 0
    while count < iterations:
        count += 1
        neighbours = neighbours_func(node)
        scores = np.zeros(shape=len(neighbours))
        for i, n in enumerate(neighbours):
            scores[i] = score_func(n, score_arg)
        idx = np.argmax(scores)
        if scores[idx] <= current_score:
            break
        current_score = scores[idx]
        node = neighbours[idx]
    return node
  