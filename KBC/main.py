#Welcoming user and printing first question. 
print("Welcome to Kaun Banega Crorepati.\nHere are the questions.")
lQues = ["""1. Which pieces are maximun in number at the start of a chess game?\n
A:Bishop  B:Rook C:Knight  D:Pawn\n""", 
        """2. How many Watts equal a Megawatt?\n
A:Ten Thousand  B:One Hundred  C:One Lakh  D:One Thousand\n""", 
        """3. If someone suffered from 'amnesia' which of the following would they be likey to do?\n
A:Forget things  B:Start Dieting  C:Get Angry  D:Always Smile\n""", 
        """4. Which part of the eye is stored in eye banks for transplant?\n
A:Pupil  B:Iris  C:Retina  D:Cornea\n""",
        """5. Which of these persons has not walked on the Moon?\n 
A:Charles Duke  B:Pete Conrad  C:James A Lovell  D:Alan Bean\n"""]
print(lQues[0])

#Asking user first question
ques0 = int(input("""If you think answer is A, Click 1.
If you think answer is B, Click 2.
If you think answer is C, Click 3.
If you think answer is D, Then click 4.\n"""))
#Evalutating if the answer 0 is correct or not. 
if ques0 == 4: #Condition1: if the ans is correct.
  print("Congratulations ! You have won Rs. 1,000. Here is next Question:")
  print(lQues[1])


  #Continuing to Question 1 if the ans1 is correct. 
  ques1 = int(input("""If you think answer is A, Click 1.
If you think answer is B, Click 2.
If you think answer is C, Click 3.
If you think answer is D, Then click 4.\n"""))
  #Evaluating if ans 1 is correct. 
  if ques1 == 3:
    print("Congratulations ! You have won Rs. 2,000. Here is next Question:")
    print(lQues[2])


    #Continuing to Question 2 if the ans1 is correct. 
    ques2 = int(input("""If you think answer is A, Click 1.
If you think answer is B, Click 2.
If you think answer is C, Click 3.
If you think answer is D, Then click 4.\n"""))
    #Evaluating if ans 2 is correct. 
    if ques2 == 1:
      print("Congratulations ! You have won Rs. 5,000. Here is next Question:")
      print(lQues[3])
    
      #Continuing to Question 3 if the ans2 is correct.
      ques3 = int(input("""If you think answer is A, Click 1.
If you think answer is B, Click 2.
If you think answer is C, Click 3.
If you think answer is D, Then click 4.\n"""))
      if ques3 == 4:
        print("Congratulations ! You have won Rs. 10,000. Here is next Question:")
        print(lQues[4])
        

        #Continuing to Question 4 if the ans 3 is correct. 
        ques4 = int(input("""If you think answer is A, Click 1.
If you think answer is B, Click 2.
If you think answer is C, Click 3.
If you think answer is D, Then click 4.\n"""))
        if ques4 == 3:
          print("Congratulations ! You have won Rs. 1,00,000. You are going home with whoping Rs. 1,00,000.")

          
#Elif and else of ques4. 
        elif ques4 <=0 or ques4 > 4: #Condition2: if the ans is invalid.
          print("Answer is invalid. Please play the game from beginning.")
        else: #Condition3: if the ans is incorrect.
          print("Wrong Answer, You are eliminated from the Game.")

        
#####Elif and else of ques3.
      elif ques3 <=0 or ques3 >4: #Condition2: if the ans is invalid.
        print("Answer is invalid. Please play the game from beginning.")
      else: #Condition3: if the ans is incorrect.
        print("Wrong Answer, You are eliminated from the Game.")


#####Elif and else of ques2.
    elif ques2 <=0 or ques2 > 4: #Condition2: if the ans is invalid.
      print("Answer is invalid. Please play the game from beginning.")
    else: #Condition3: if the ans is incorrect.
        print("Wrong Answer, You are eliminated from the Game.")


#####Elif and else of ques1.
  elif ques1 <=0 or ques1 > 4:  #Condition2: if the ans is invalid.
    print("Answer is invalid. Please play the game from beginning.")
  else: #Condition3: if the ans is incorrect.
    print("Wrong Answer, You are eliminated from the Game.")

#####Elif and else of ques0.
elif ques0 <=0 or ques0 > 4: #Condition2: if the ans is invalid.
  print("Answer is invalid. Please play the game from beginning.")
  
else: #Condition3: if the ans is incorrect.
  print("Wrong Answer, You are eliminated from the Game. ")