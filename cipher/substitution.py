

def substitution_score(key, text):
    return score(find_ngrams(substitution_cipher.decrypt(text, key), 2, dic = False))

def substitution_get_neighbours(key):
    neighbours = list(np.zeros(shape=325))
    i = 0
    for i1 in range(26):
        for i2 in range(i1 + 1, 26):
            neighbours[i] = swap(key, i1, i2)
            i += 1
    return neighbours