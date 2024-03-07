import os


def create_files(path):
    os.chdir(path)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        if letter.upper() == "Z":
            open(f"{letter}.txt", "x", encoding="utf-8")
            break
        open(f"{letter}.txt", "x", encoding="utf-8")

    print("Files created")


#num = input("Enter last letter to be created: ")
path1 = "/Users/EmbaSSD/Downloads/Labs/L6/Files"
create_files(path1)