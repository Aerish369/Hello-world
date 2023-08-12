from datetime import date

#* Class of BCA students (Second Semester) with datas related to them.

class Students:
    total_Students = 0
    fees_per_sem = 45000

    def __init__(self, fname, lname, age, learning, semester):
        self.fname = fname 
        self.lname = lname
        self.age = age
        self.learning = learning
        self.semester = semester
        Students.total_Students += 1

    def fullname(self): # returns full name 
        return '{} {}'.format(self.fname, self.lname)

    def email(self): # returns email
        return '{}.{}@tuicms.edu.np'.format(self.fname, self.lname).lower()

    def total_fee(self): # returns total fee to be paid
        return 8 * self.fees_per_sem

    def due_fee(self): # returns due fee to be paid
        return (8 - self.semester) * self.fees_per_sem

    def paid_fee(self): # returns fee paid till
        return self.semester * self.fees_per_sem

    @classmethod # Classmethods are used to execute anything on class level not on instance level. They can be used as alternative constructor as well. 
    def set_fees_per_sem(cls, fee):
        cls.fees_per_sem = fee

    #* if you don't acess the instance or class in a function. Then static method should be created. 
    @staticmethod
    def is_studyday(day):
        if day.weekday() == 5:
            return False
        return True

    #! Alt Constructor
    @classmethod
    def fromStr(cls, string):
        fname, lname, age, learning, semester = string.split('-')
        return cls(fname, lname, age, learning, semester)

    def __repr__(self): #* For unambigious info about object. Specially for programmers
        return 'Students({}, {}, {}, {}, {})'.format(self.fname, self.lname, self.age, self.learning, self.semester)

    def __str__(self): #* For Readable info about the object. Specially for Users
        return '{} - {}'.format(self.fullname(), self.email())

    def __len__(self): #* Returns length of the fullname of the object called upon
        return len(self.fullname())

    def __call__(self): #* Used object to act like function to operate specific task upon calling. 
        return print(f'{self.fullname()} is student of BCA in ICMS. S/he is in {self.semester} semester.')

class Sing_Member(Students):
    def __init__(self, fname, lname, age, learning, semester, genre): 
        super().__init__(fname, lname, age, learning, semester) #* Inheriting different aruguements of Students Class
        self.genre = genre

    
sId1 = Students('Aashish', 'Aryal', 18, 'Python', 2)
sId2 = Students('Ayush', 'Tamang', 18, 'Django', 3)
sId3 = 'Anil-Magar-18-HTML-2'
sId3 = Students.fromStr(sId3)
sId4 = Sing_Member("Sita", 'Tamang', 19, 'Git', 2, 'Sastriya')


sId4()









Students.set_fees_per_sem(50000) # Usecase of class method to set free per sem different from it's default value in class. 


# Using static method
# today = date.today()
# print(Students.is_studyday(today))
# print(today)




