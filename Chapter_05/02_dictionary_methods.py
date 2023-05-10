myDict = {
    "Fast": "In a quick manner",
    "Aerish": "Entrepreneur",
    "Marks": [2,3,5],
    "anotherDict": {'hero': 'A person with good doings'},
    2: 8
}

#Dictionary_methods
print(list(myDict.keys())) # This prints the keys of the dictionary. 
print(list(myDict.values())) # This prints the values of the dictionary.
print(list(myDict.items())) # This prints the (key,values) for all the contents of the dictionary.
print(myDict)
updateDict = {
    "Villian": "Anti-Hero",
}
myDict.update(updateDict) # This updates the dictionary by adding key-value pairs from updateDict. 
print(myDict)

print(myDict.get("Aerish")) #Prints value associated with key "Aerish".
print(myDict["Aerish"]) #Prints value associated with key "Aerish". 

#The difference between .get and [] syntax in dictionary. 
print(myDict.get("Aerish1")) #Returns none as Aerish1 is not present in the myDict. 
print(myDict["Aerish1"]) # This throws an error as it is not presented in the myDict. 