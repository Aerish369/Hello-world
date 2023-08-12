class Students:

    def __init__(self, maths, science, english):

        self.maths = maths
        self.science = science
        self.english = english

    def __call__(self):
        return 'This contains marksof subject maths - {},science -  {} and english - {} respectively.'.format(self.maths, self.science, self.english)
    
    def __add__(self, secondself):
        '''This method adds the specific value of the instance with it's respective value'''
        maths = self.maths + secondself.maths
        science = self.science + secondself.science
        english = self.english + secondself.english

        return (maths, science, english)
    



x1 = Students(80,78,50)
x2 = Students(23, 13, 50)
print(x1 + x2)