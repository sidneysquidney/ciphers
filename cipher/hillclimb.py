import numpy as np

import cipher_functions

# score args will probably just be the ciphertext, but make sure it's in a tuple: score_args=(ciphertext)
def hillclimb(start_node, score_func, neighbours_func, score_args=(), iterations=5):
    node = start_node
    current_score = score_func(node, *score_args)
    count = 0
    for it in range(iterations):
        while True:
            count += 1
            neighbours = neighbours_func(node)
            # scores = [None]*len(neighbours)
            scores = np.zeros(shape=len(neighbours))
            for i, n in enumerate(neighbours):
                scores[i] = score_func(node, *score_args)
            idx = np.argmax(scores)

            if scores[idx] < current_score:
                break
            current_score = scores[idx]
            node = neighbours[idx]
    return node

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