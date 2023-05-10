question=[["1. Which pieces are maximun in number at the start of a chess game?"],["2. How many Watts equal a Megawatt?"],["3. If someone suffered from 'amnesia' which of the following would they be likey to do?"],["4. Which part of the eye is stored in eye banks for transplant?\
"]]
option=[["A:Bishop  B:Rook C:Knight  D:Pawn"],["A:Ten Thousand  B:One Hundred  C:One Lakh  D:One Thousand"],["A:Forget things  B:Start Dieting\ C:Get Angry  D:Always Smile"],["A:Pupil  B:Iris  C:Retina  D:Cornea"] ]

answer=[4,3,1,4]

prize = [1000, 2000, 5000, 10000]
i=0
while True:
    print(f"Question-->{question[i]}")
    print(f"Option-->{option[i]}")
    user=int(input("Enter 1,2,3 or 4\n"))

    if isinstance(user,int) and user>=1 and user<=4:
        if user==answer[i]:
            print(f"Yes indeed ,The answer the the question no : {i+1} is {answer[i]}\n")
            print(f"You've won {prize[i]}")
            i+=1
            if i==4:
               print("Congrats You've solved all the question ")
               break
        else:
            print("Incorrect answer\n")
            break

    else:
        print("Invalid input\nPlease Enter Integers not the string")