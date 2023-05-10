comment = input("Comment: \n")

spam = False

if("make a lot of money" in comment):
    spam = True
elif("buy now" in comment):
    spam = True
elif("subscribe now" in comment):
    spam = True
elif("watch this" in comment):
    spam = True
elif("click this" in comment):
    spam = True
else: 
    spam = False

if(spam):
    print("This text is spam.\n")
else:
    print("This text is not spam.\n")