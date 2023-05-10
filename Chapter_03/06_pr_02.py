letter = '''Dear <|NAME|>,
Greeting from Intellectify. I'm excited to tell you about your selection.
You are selected !
Have a Great day ahead.
Kind Regards,
Aerish Aryal
Date: <|DATE|>
'''
name = input("Enter your name.\n")
date = input("Enter date. \n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)