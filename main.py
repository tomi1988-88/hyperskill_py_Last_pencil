import string
from random import randint

pencils = input("How many pencils would you like to use:\n")
while True:
    if not pencils.isdigit():
        pencils = input("The number of pencils should be numeric\n")
    elif not (int(pencils) > 0):
        pencils = input("The number of pencils should be positive\n")
    else:
        pencils = int(pencils)
        break

name = input("Who will be the first (John, Jack):")
while True:
    if name in ("John", "Jack"):
        break
    else:
        name = input("Choose between 'John' and 'Jack'\n")

print("|" * pencils)

player1 = name
player2 = "Jack" if player1 == "John" else "John"

counter = 0
while True:

    if counter % 2 == 0:
        curr_player, sec_player = player1, player2
    else:
        curr_player, sec_player = player2, player1

    if curr_player == "John":
        print(f"John's turn:")
    else:
        print(f"Jack's turn!")

    if curr_player == "John":
        pen_to_drop = input()
    else:
        if pencils % 4 == 0:
            pen_to_drop = "3"
        elif pencils % 4 == 3:
            pen_to_drop = "2"
        elif pencils % 4 == 2:
            pen_to_drop = "1"
        else: 
            if pencils == 1:
                pen_to_drop = "1"
            else:
                pen_to_drop = str(randint(1, 3))

    if curr_player == "Jack":
        print(pen_to_drop)

    while True:
        if pen_to_drop in string.digits and 0 < int(pen_to_drop) < 4:
            pen_to_drop = int(pen_to_drop)
            break
        else:
            pen_to_drop = input("Possible values: '1', '2' or '3'\n")

    while True:
        if pen_to_drop <= pencils:
            pencils -= pen_to_drop
            break
        else:
            pen_to_drop = int(input("Too many pencils were taken\n"))

    print("|" * pencils)

    if pencils == 0:
        print(f"{sec_player} won!")
        break

    counter += 1
