question=[["1. Which pieces are maximun in number at the start of a chess game?"],["2. How many Watts equal a Megawatt?"],["3. If someone suffered from 'amnesia' which of the following would they be likey to do?"],["4. Which part of the eye is stored in eye banks for transplant?\
"]]
option=[["A:Bishop  B:Rook C:Knight  D:Pawn"],["A:Ten Thousand  B:One Hundred  C:One Lakh  D:One Thousand"],["A:Forget things  B:Start Dieting\ C:Get Angry  D:Always Smile"],["A:Pupil  B:Iris  C:Retina  D:Cornea"] ]

answer=["d","c","a","d"]

for i in range(len(question)):
    print(f"Question-->{question[i]}")
    print(f"Option-->{option[i]}")
    user=str(input("Enter a,b,c or d")).lower()

    if isinstance(user,str):
        if user==answer[i]:
            print(f"Yes indeed ,The answer the the question no : {i+1} is {answer[i]}\n")
        else:
            print("Incorrect answer\n")
            break

    else:
        print("Invalid input ")
        break