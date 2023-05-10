myDict = {
    "Pani": "Water",
    "Miti": "Date",
    "Janma": "Birth",
    "Kagaj": "Paper",
    "Aaina": "Mirror",
}
print("Options are: ", myDict.keys())
a = input("Enter the Nepali Word\n")
# print("The meaning of your word is: ", myDict[a])
print("The meaning of your word is: ", myDict.get(a)) # THis line will not throw an erroe if the key is not in the list. 