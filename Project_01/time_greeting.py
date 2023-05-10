import time

timestamp = time.strftime('%H:%M:%S') #Printing time of Local PC
print(timestamp)

#Typecasting time which are in the string into integers. 
hour = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

#Evaluating if the time is Morning, Afternoon or Evening and printing greetings accordingly. 

if(hour<12):
    print("Good Morning Sir!")
elif(hour<18):
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")
