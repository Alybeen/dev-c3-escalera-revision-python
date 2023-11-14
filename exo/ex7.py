import os
import string


def read_file(path_file: string):
    size = os.path.getsize(path_file)
    if size == 0:
        return
    else:
        file = open(path_file, "r")
        lines = file.readlines()
        file.close()
        number_words = []
        for line in lines:
            number_words += line.split()
        return len(number_words)

if read_file("test.txt") is not None:
    print(f'nombre de mots : {read_file("test.txt")}')
else:
    print("ce fichier est vide")
