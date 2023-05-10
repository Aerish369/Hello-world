##This is the copy of the main.py code but with comments generated from ChatGPT. It is to help reader understand the logic behind the game. 

import random # import the random module

# function to determine the winner of the game
def gamewin(comp, you):
    # if the computer and player have chosen the same option, return None
    if comp == you:
            return None
    elif comp == 's': # if the computer has chosen snake
        # if the player has chosen water, return False (player wins)
        if you == 'w':
            return False
        # if the player has chosen gun, return True (computer wins)
        elif you == 'g':
            return True
    elif comp == 'w': # if the computer has chosen water
        # if the player has chosen gun, return False (player wins)
        if you == 'g':
            return False
        # if the player has chosen snake, return True (computer wins)
        elif you == 's':
            return True
    elif comp == 'g': # if the computer has chosen gun
        # if the player has chosen snake, return False (player wins)
        if you == 's':
            return False
        # if the player has chosen water, return True (computer wins)
        elif you == 'w':
            return True

# generate a random number between 1 and 3
randNo = random.randint(1, 3)
print(randNo)
# if the random number is 1, set comp to 's' (computer has chosen snake)
if randNo == 1:
    comp = 's'
# if the random number is 2, set comp to 'w' (computer has chosen water)
elif randNo == 2:
    comp = 'w'
# if the random number is 3, set comp to 'g' (computer has chosen gun)
elif randNo == 3:
    comp = 'g'
# print prompt for player's choice
print("Comp Turn: Snake(s), Water(w) or Gun(g)\n")
# get player's choice as input
you = input("Your Turn: Snake(s), Water(w) or Gun(g)?\n")

# call the gamewin function and store the result in 'a'
a = gamewin(comp, you)

# print the computer's choice
print(f"Computer choose {comp}\n")
# print the player's choice
print(f"You choose {you}\n")

# check the result of the game and print the result
if a == None:
    print("The game is tie. ")
elif a: 
    print("You won! ")
else: 
    print("You lose! ")
