from .student import *
from .loadtpl import *
class starosta(student):
    def __init__(self,q):
        super().__init__(q)
        self.number = ''
    def show(self):
       print(loadtpl('showstarosta').format(self.second, self.first, self.father, self.age,self.fac,self.number,self.q['student'].value,self.iid))
    def edit(self,q):
        super().edit(q)
        self.number = q['number'].value
    def addform(self):
                print(loadtpl('addformstarosta').format (self.second,self.first,self.father,self.age,self.fac,self.number,self.q['student'].value))
    def editform(self, q):
                print(loadtpl('editformstarosta').format (self.second, self.first,self.father, self.age,self.fac,self.number,q['iid'].value,q['student'].value))
