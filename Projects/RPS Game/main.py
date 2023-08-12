from random import randint

bot = randint(1, 3) #prompting random number from 1 to 3 to use as computer's side of the game

#Taking input from player1

pl1 = int(input("""
                    Click 1 for Scissors,
                    Click 2 for Papers, 
                    Click 3 for Rock,
                    Enter the number: """))
if (0>pl1 or pl1>3): #Giving error for input other than 1, 2, 3.
    raise ValueError("Invalid Input. Please enter valid input.")

#Checking on win, draws and loses from pl1 perspective. 
if pl1==1 and bot==1:
    print("You: Scissors, Bot: Scissors, The Game is draw.")

if pl1==1 and bot==2:
    print("You: Scissors, Bot: Paper, You won the Game.")

if pl1==1 and bot==3:
    print("You: Scissors, Bot: Rock, You lose the Game.")

if pl1==2 and bot==1:
    print("You: Paper, Bot: Scissors, You lose the Game.")

if pl1==2 and bot==2:
    print("You: Paper, Bot: Paper, The Game is draw.")

if pl1==2 and bot==3:
    print("You: Paper, Bot: Rock, You won the Game.")

if pl1==3 and bot==1:
    print("You: Rock, Bot: Scissors, You won the Game.")

if pl1==3 and bot==2:
    print("You: Rock, Bot: Paper, You lose the Game.")

if pl1==3 and bot==3:
    print("You: Rock, Bot: Rock, The Game is draw.")



