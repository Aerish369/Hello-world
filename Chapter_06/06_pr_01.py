#Prompting user for four interger values. 
num1 = int(input("Enter a number 1: \n"))
num2 = int(input("Enter a number 2: \n"))
num3 = int(input("Enter a number 3: \n"))
num4 = int(input("Enter a number 4: \n"))

if(num1>num4):  #Comparing num1 and num4. 
    f1 = num1
else:
    f1 = num4

if(num2>num3): #Comparing num2 and num3. 
    f2 = num2
else:
    f2 = num3

if(f1>f2):   #comparing f1 and f2. f1 is the result of num1>num4. f2 is the result of num2>num3. 
    print(f1, "is greatest number. ")  #printing the results. 
else:
    print(f2, "is greatest number. ")
