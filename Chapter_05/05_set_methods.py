b = set() # This will create empty set. 
print(type(b))

##Adding values to an empty set. 
b.add(1)
b.add(2)
b.add(3) #Adding a value repeadly doesn't changes a set. 
b.add((4, 3)) #It accepts tuple as it is immutable. 
#b.add([2, 3, 4]) #Can't add mutable like list.
print(b)

##Length of the set. 
print(len(b)) #Prints the length of a set. 

##Removal of the items.
b.remove(3) #Removes 3 from the set b. 
#b.remove(400) #Throws an error while trying to remove 15, which is not present in the set. 
print(b)

##Pops elements of the set. 
print(b.pop())
print(b)