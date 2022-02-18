"""
Name: Scarlett Duncan
hw5.py

Problem: Create codes to practice using strings to produce various outputs

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    name = input("enter a name (first last): ")
    split = name.split()
    print(split[-1], ",", split[0])


def company_name():
    domain = input("enter a domain:" )
    company = domain.split(".")
    print(company[1])


def initials():
    student_number = eval(input("how many students are in the class?"))
    for i in range(student_number):
        words = "what is the name of student " + str(i+1) + "?"
        name = input(words)
        name_seperate = name.split()
        first_name = name_seperate[0]
        last_name = name_seperate[-1]
        initial_first = first_name[0]
        initial_last = last_name[0]
        print(initial_first+initial_last)



def names():
    names_list = input("Enter a list of names: ")
    names_split = names_list.split(",")
    number = len(names_split)
    for i in range(number):
        name_seperate = names_split[i]
        name_split_again = name_seperate.split()
        first_name = name_split_again[0]
        last_name = name_split_again[-1]
        first_initial = first_name[0]
        last_initial = last_name[0]
        print(first_initial+last_initial, end=" ")

def thirds():
    sentence_number = eval(input("enter the number of sentences:"))
    acc = " "
    for i in range(sentence_number):
        words = "enter sentence " + str(i+1) +":"
        sentence = input(words)
        every_third = sentence[0:-1:3]
        acc = acc + every_third + "\n"
    print(acc)


def word_average():
    sentence = input("enter a sentence: ")
    sentence_split = sentence.split()
    word_count = len(sentence_split)
    acc = 0
    for i in range(word_count):
        word = sentence_split[i]
        letter_count = len(word)
        acc = acc + letter_count
    average = acc / word_count
    print(average)


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    sentence_split = sentence.split()
    number_words = len(sentence_split)
    acc = " "
    for i in range(number_words):
        word = sentence_split[i]
        first_letter = word[0]
        other_letters = word[1:]
        ending = "ay"
        pig_latin = other_letters + first_letter + ending
        acc = acc + " " + pig_latin
    print(acc)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
