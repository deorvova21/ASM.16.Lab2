import cgi
from .Student import *
from .LoadTpl import *

class Graduate(Student):
    def __init__(self,q):
        super().__init__(q)
        self.dipl=''
        self.q=self.q
        
    def Edit(self,q):
        self.name = q['name'].value
        self.year = q['year'].value
        self.dipl = q['dipl'].value
        
    def ShowForm(self):
        print(LoadTpl('addgrad').format(self.q['student'].value, self.name, self.year, self.dipl))

    def Change(self,q):
        print(LoadTpl('editgrad').format(q['student'].value, q['i'].value, self.name, self.year, self.dipl))

    def Show(self, q, i):
        print(LoadTpl('showgrad').format(q['student'].value, i, self.name, self.year, self.dipl))


