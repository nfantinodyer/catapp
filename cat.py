import random

def get_cat_phrase():
    file1 = open("catphrase.txt", "r")
    lines = file1.readlines()

    dialog = []

    for line in lines:
        dialog.append(line)

    return random.choice(dialog)

print("Type in meow to get a cat phrase (q to exit):")
while True:
    user_input = input()
    if user_input == "meow":
        print(get_cat_phrase())
    elif user_input == "q":
        break
    else:
        print("Type in meow to get a cat phrase:\n")