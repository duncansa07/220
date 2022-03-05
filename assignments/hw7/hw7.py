"""
Name: Scarlett Duncan
hw7.py

Problem: create various functions that produce a given outcome in order to practice the use of functions

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math

def number_words(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    words = file.read()
    output_file = open(out_file_name, "w")
    for i in range(len(words)):
        print(i+1, words[i],  file=output_file)


def hourly_wages(in_file_name, out_file_name):
    employee_info = open(in_file_name, "r")
    employee_lines = in_file_name.readlines()
    numb_employee = len(employee_lines)
    for i in range(numb_employee):
        employee_x = numb_employee[i]
        total_pay = employee_x[2] * employee_x[3] + 1.65 * employee_x[3]
        total_pay_format = ("${:.2f}").format(total_pay)
        output_file = open(out_file_name, "w")
        output = employee_info[1] + employee_info[0] + total_pay_format
    print(output, file=output_file)


def calc_check_sum(isbn):
    isbn_cleaned = isbn.replace("-", "")
    sum_total = 0
    for i in range(len(isbn_cleaned)+1):
        isbn_int_one = int(isbn_cleaned[-i])
        sum_isbn = (i) * isbn_int_one
        sum_total = sum_isbn + sum_total
    print(sum_total)


def send_message(file_name, friend_name):
    file_opened = open(file_name, "r")
    words = file_opened.readlines()
    output_file_name = friend_name + ".txt"
    output = open(output_file_name, "w")
    print(words, file=output_file_name)


def encode(message, key):
    length = len(message)
    for i in range(length):
        message_encoded = ""
        new_numb = ord(message[i]) + key
        new_letter = chr(new_numb)
        message_encoded = message_encoded + new_letter
    return message_encoded


def send_safe_message(file_name, friend_name, key):
    info = open(file_name, 'r')
    output_file_name = friend_name + '.txt'
    output_file = open(output_file_name, 'w')
    input_file_lines = file_name.readlines()
    for i in range(len[input_file_lines]):
        from encryption import encode
        encode(input_file_lines[i], key)
        print(message_encoded, file=output_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    from encryption import encode_better
    message = file_name.read()
    key = pad_file_name.read()
    output_file_name = friend_name + '.txt'
    output_file = (output_file_name, 'w')
    encode_better()


if __name__ == '__main__':
    pass
