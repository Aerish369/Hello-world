#Python Object-Oriented Programming: Classes and Instances

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps +=1

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



    
dev_1 = Employee('Aerish', 'Aryal', 750000)
dev_2 = Employee('Test', 'User', 500000)




print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)





