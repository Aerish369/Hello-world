
import shutil

print("This is original file. ")

#! This (shutil.copy()) copies the file from the pathway to given location. 
#* shutil.copy("main.py", r"C:\Users\aryal\OneDrive\Desktop\hero.py") 

#! This helps to move the file from the pathway to given location.
#* shutil.move("hero.py", r"C:\Users\aryal\OneDrive\Desktop\Aerish\Python\Shutil Module\main.py")

#! This helps to copy the file including metadata.abs
shutil.copy2("main.py", "file/copied.py")