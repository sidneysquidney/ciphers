

def vinegar_score(key, text):
    return score(find_ngrams(vinegar_cipher.decrypt(text, key), 2, dic = False))

def vinegar_get_neighbours(key):
    neighbours = list(np.zeros(shape=len(key) * 26))
    for i1 in range(len(key)):
        for i in range(len(alphabet)):
            neighbours[i1 * 26 + i] = key[:i1] + alphabet[i] + key[i1 + 1:]
    return neighbours
