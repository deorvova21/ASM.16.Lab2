import cgi
from .LoadTpl import *

class Student:
    def __init__(self,q):
        self.name=''
        self.year=''
        self.q=q
        
    def Edit(self,q):
        self.name = q['name'].value
        self.year = q['year'].value
        
    def ShowForm(self):
        print(LoadTpl('addstud').format(self.q['student'].value, self.name, self.year))

    def Change(self, q):
        print(LoadTpl('editstud').format(q['student'].value,q['i'].value, self.name, self.year))       

    def Show(self, q, i):
        print(LoadTpl('showstud').format(q['student'].value,i, self.name, self.year))
  




    
    
