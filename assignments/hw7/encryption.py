def encode(message, key):
    length = len(message)
    for i in range(length):
        message_encoded = ""
        new_numb = ord(message[i]) + key
        new_letter = chr(new_numb)
        message_encoded = message_encoded + new_letter
    return message_encoded


def encode_better(message, key):
    key = key.upper()
    length_message = len(message)
    length_key = len(key)

    for i in range(length_message):
        step_1 = ord(message[i]) - 65
        step_2 = ord(key[i % length_key]) - 65
        step_3 = step_1 + step_2
        step_4 = (step_3 % 26) + 65
        fin = chr(step_4)
        print(fin, file=output_file)