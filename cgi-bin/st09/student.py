from .loadtpl import *
class student:
    def __init__(self,q):
        self.q=q
        self.iid=''
        self.second = ''
        self.first = ''
        self.father =''
        self.age = ''
        self.fac = ''
    def show(self):
         print(loadtpl('showstudent').format(self.second, self.first, self.father, self.age,self.fac,self.q['student'].value,self.iid))
    def edit(self,q):
        
        self.second = q['second'].value
        self.first = q['first'].value
        self.father = q['father'].value
        self.age = q['age'].value
        self.fac = q['fac'].value
        
    def addform(self):
                print(loadtpl('addformstudent').format (self.second,self.first,self.father,self.age,self.fac,self.q['student'].value))
    def editform(self, q):
                print(loadtpl('editformstudent').format (self.second, self.first,self.father, self.age,self.fac,q['iid'].value,q['student'].value))
