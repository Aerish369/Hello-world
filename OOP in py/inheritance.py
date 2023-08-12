#Python Object-Oriented Programming: Classes and Instances

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last).lower()
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee): #Inherited New class named Developer which is inheriting Employee.
    raise_amount = 1.10

    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang

class Manager(Employee): #Manager class with employees under supervision
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp): #Adding the employees(if not)
        if emp not in self.employees:
            self.employees.append(emp)
    
    def rmv_emp(self, emp): #Removing the employees (if already there)
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self): # Prints All employee managed by Manager
        for emp in self.employees:
            print('-->', emp.fullname())

    
dev_1 = Developer('Aerish', 'Aryal', 750000, 'Python')
dev_2 = Developer('Test', 'User', 500000, 'TypeScript')
emp_1 = Employee('Ladu', 'Lalit', 350000)
mgr_1 = Manager('Robert', 'Kyosaki', '1000000', [dev_2])

mgr_1.add_emp(emp_1)
mgr_1.add_emp(dev_1)
               


mgr_1.rmv_emp(dev_2)

mgr_1.print_emp()

#print(isinstance(mgr_1, Developer)) #Tells if a instance is inherited from given class or not. 
# print(issubclass(Developer, Manager))






# print(dev_1.email)
# print(dev_1.pro_lang)


# print(dev_1.first)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
