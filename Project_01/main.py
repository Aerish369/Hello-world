import random

#Snake Water and Gun Game.

#Making function with all the possibilities. 
def gamewin(comp, you):
    #If two values are equal, declare a tie.
    if comp == you:
            return None
    #Check for all possibilities When computer choose s.
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
    #Check for all possibilities When computer choose w.
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
        
    #Check for all possibilities When computer choose g.
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

randNo = random.randint(1, 3) #Using random module's randint to generate random integer from (1, 3).

#Turning 1,2,3 into s,w,g.
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

#Prompting user for input.
you = input("Your Turn: Snake(s), Water(w) or Gun(g)?\n")

#Calling function. 
a = gamewin(comp, you)

#Printing what computer and player choose. 
print(f"Computer choose {comp}\n")
print(f"You choose {you}\n")

#Printing results. 
if a == None:
    print("The game is tie. ")
elif a: 
    print("You won! ")
else: 
    print("You lose! ")