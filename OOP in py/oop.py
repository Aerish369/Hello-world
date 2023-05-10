class Person:
    name = "Aerish"
    occupation = "Entrepreneur"
    Networth = 100000
    def info(self):
        print(f"{self.name} is an {self.occupation}.")

i = Person()
i.name = "Harry"
i.occupation = "Investor"

j = Person() 
j.name = "Susmita"
j.occupation = "Trader"

i.info()
j.info()

# print(i.name, ',' , i.occupation)
# print(Person.name)

class Employee: 
    def __init__(self, name, occ):
        self.name = name
        self.occ = occ

    def info(self):
        print(f'{self.name} is a {self.occ}.')


Emp1 = Employee('Aerish', 'HR')
print(Emp1.name)
Emp1.info(  )