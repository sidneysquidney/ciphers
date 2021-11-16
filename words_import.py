

def import_words(file_name):
    with open(file_name) as words_file:
        words = words_file.read()
    w = words.split('\n')
    return w

most_common_words = import_words('google-10000-english-no-swears.txt')


