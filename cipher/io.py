import json
import pandas as pd
import numpy as np

# dictinary and list of most frequent monograms in the english language
def read_monograms(file='texts/monograms.json'):
    with open(file) as f:
        monograms = json.load(f)
    monograms_list = [l.lower() for l in monograms.keys()]
    return monograms_list 

def read_bigrams(filename):
    df = pd.read_csv(filename, delimiter=' ', names=['bigrams','count'], keep_default_na=False)
    total = sum(df['count'])
    bigrams, count = df['bigrams'], df['count'] / total
    frequency_dict = {bigrams[i].lower(): np.log(count[i]) for i in range(len(bigrams))}
    return frequency_dict

# returns the string from a text file, all in lower case
def turn_into_string(file_name):
    with open(file_name, 'r') as file:
        content = file.read().replace('\n', ' ')
    return content.lower()

def read_wordlist(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines