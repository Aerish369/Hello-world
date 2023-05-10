sub1 = int(input("Enter first subject marks: \n"))
sub2 = int(input("Enter second subject marks: \n"))
sub3 = int(input("Enter third subject marks: \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You have failed bacause you have less than 33 in one of the subjects. Better study next time!")

elif(sub1+sub3+sub3)/3 < 40:
    print("You have failed due to total percentage less than 40. Better study next time!")
else:
    print("Congratulations! You have successfully passed the examination. ")