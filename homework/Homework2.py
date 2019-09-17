import random

options = "NSEW"
list_main = [random.choice(options) for i in range(6)]
list_copy = list_main[:]

moves = 0
hp = 3

while True:
    if moves == 10:
        hp -= 1
        moves = 0
    if not hp:
        print("YOU DIED!")
        break
    if not list_main.__len__():
        print("YOU ESCAPED!")
        break
    print("\n{} rooms left!".format(list_main.__len__()))
    move = input("Enter a move [N/S/E/W] >> ").upper()
    if move not in options:
        print("Invalid move!")
        continue
    moves += 1
    if move == list_main[0]:
        print("Continue!")
        list_main.__delitem__(0)
    else:
        print("WRONG PATH")
        list_main = list_copy[:]
        hp -= 1

