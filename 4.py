import os


def open_path(path):
    file = open(path)
    file_contents = len(file.readlines())
    return file_contents


path = "/Users/EmbaSSD/Downloads/Labs/L6/TEXT.TXT"
print(open_path(path))