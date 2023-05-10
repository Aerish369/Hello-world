class Employee:
    def __init__(self) -> None:
            self.__name = 'Aerish'

a = Employee()
#print(a.__name) # Cannot be accessed directly
print(a._Employee__name) #Can be accessed indirectly


#### Note there are nothing like private and public modifier. But there is convention in python community that __Variable is private.
#  
# name is public access modifier.
# __name is private modifier.
# _name is protected modifier.

## _myClass__variable --> This is called name-mangling to access private access modifier. 