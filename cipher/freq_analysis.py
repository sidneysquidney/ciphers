
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def index_of_coincidence(text):
    pass


def find_ngrams(text, ngram_length):
    text = ''.join([l for l in text.lower() if l in ALPHABET])
    number_ngrams = len(text) - ngram_length + 1
    ngrams = [None for g in range(number_ngrams)]
    for i in range(len(ngrams)):
        ngrams[i] = text[i: i + ngram_length]  
    return ngrams


def ngram_score(ngrams):
    pass