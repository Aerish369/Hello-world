class Person:
    def __init__(self, name, occ):
        print(f"Hello Aerish")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is an {self.occ}.")

a = Person("Harry","Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# a.name = "Sahara"
# a.occupation = "Teacher"
# a.info()