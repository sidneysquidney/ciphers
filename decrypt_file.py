from cipher import decrypt, io
# from cipher import io


def main():
    text = io.turn_into_string("texts/bee_movie_encrypted.txt")
    bigrams = io.read_bigrams('texts/bigrams.csv')

    if decrypt.is_caesar(text, bigrams):
        print("I think it's a caesar cipher...")
        decrypted, key = decrypt.caesar_decipher(text, bigrams, get_key=True)
    elif decrypt.is_vinegar(text):
        print("I think it's a vinegere cipher...")
        decrypted, key = decrypt.vinegar_decipher(text, bigrams)
    else:
        print("I think it's a substitution cipher...")
        monograms = io.read_monograms('texts/monograms.json')
        common_words = io.read_wordlist('texts/google-10000-english-no-swears.txt')
        decrypted, key = decrypt.substitution_decipher(text, monograms, bigrams, common_words, get_keys=True)
    print('Decrypted text:')
    print(decrypted)
    print('\nKey:')
    print(key)


if __name__ == "__main__":
    main()