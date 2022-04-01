"""
Name: Scarlett Duncan
hw9.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def get_words(file_name):
    file = open(file_name, 'r')
    words = file.readlines()
    return words


def get_random_word(words):
    word_number = randint(0, len(words)-1)
    secret_word = words[word_number].strip("\n")
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    word = ""
    for letter in secret_word:
        if letter in guesses:
            word = word + letter + " "
        else:
            word = word + "_ "
    new_word = word.strip()
    return new_word

def won(guessed):
    dashes = guessed.count("_")
    if dashes == 0:
        return True
    else:
        return False


def play_graphics(secret_word):
    f


def play_command_line(secret_word):
    guesses = []
    remainder = 6
    print("already guessed: [{}]".format(guesses))
    print("guesses remaining: {}".format(remainder))
    make_hidden_secret(secret_word, guesses)
    while remainder > 0:
        letter = input("enter a letter:")
        already = already_guessed(letter, guesses)
        if already:
            print("already guessed")
        if not already:
            guesses.append(letter)
            if letter_in_secret_word(letter, secret_word):
                return None
            else:
                remainder = remainder - 1
        word = make_hidden_secret(secret_word, guesses)
        print(word)
        print("already guessed: [{}]".format(guesses))
        print("guesses remaining: {}".format(remainder))


if __name__ == '__main__':
    pass
    #play_command_line(secret_word)
    # play_graphics(secret_word)
