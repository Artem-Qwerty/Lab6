import os


def copy_content(file, destination):
    copied = open(file, 'r')
    lines = copied.readlines()
    destination = open(destination, 'a')
    for line in lines:
        destination.write(line + "\n")

    print("Copied")


path = "/Users/EmbaSSD/Downloads/Labs/L6/7/from.txt"
dest = "/Users/EmbaSSD/Downloads/Labs/L6/7/to.txt"
copy_content(path, dest)