
import shutil

print("This is original file. ")

#! This (shutil.copy()) copies the file from the pathway to given location. 
#* shutil.copy("main.py", r"C:\Users\aryal\OneDrive\Desktop\hero.py") 

#! This helps to move the file from the pathway to given location.
#* shutil.move("hero.py", r"C:\Users\aryal\OneDrive\Desktop\Aerish\Python\Shutil Module\main.py")

#! This helps to copy the file including metadata.abs
#* shutil.copy2("main.py", "file/copied.py")

#! This helps to copy a directory or file from one path to another.
#* shutil.copytree("file", "farzifile")

#! Copying file into 5 different files from 0 to 4
#? for i in range(5):
#?     shutil.copytree("file", f"{i}")

#! Removing all the files from 0 to 4 
#? for i in range(5):
#?     shutil.rmtree(f"{i}")



   
