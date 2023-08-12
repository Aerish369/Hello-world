
#! *args is arbitary argument which takes multiple arguments. 

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

#* print(sum(12, 23, 43, 23, 34))


def getName(*args):
    for i in args:
        print(i, end=" ")


#! **kwargs is also arbitary argument which takes multiple key value pair. 

def getLocation(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")


#* getLocation(Country="Nepal",
#*             State="Bagmati",
#*             District="Kathmandu",
#*             Locality="Kapan")



def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=", ")


shippingLabel("Shrinkhala", "Khatiwada", 
            country= "Nepal",
            state="Bagmati",
            district="Makawanpur",
            locality="Hetauda")








