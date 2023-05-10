class Employee:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
    
    def showdetails(self):
        print(f"The name of Employee: {self.id} is {self.name}.")

class Programmer(Employee):
    def showlang(self):
        print("The default language is python. ")





emp1 = Employee('Rohan Das', 420)
emp1.showdetails()
emp2 = Programmer('Harry Sharma', 230)
emp2.showdetails()
emp2.showlang()


