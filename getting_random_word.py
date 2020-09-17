import random


def random_word():
    random_number = random.randint(0, 999)
    words_data = open("words.txt", "r")
    i = 0
    while i < random_number:
        words_data.readline()
        i += 1
    output = words_data.readline()
    words_data.close()
    return output

