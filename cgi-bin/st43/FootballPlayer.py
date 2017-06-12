import cgi
from .LoadTpl import *

class FootballPlayer:
    def __init__(self,q):
        self.name=' '
        self.surname=' '
        self.year=' '
        self.citizenship=' '
        self.q=q

    def Edit(self,q):
        self.name = q['name'].value
        self.surname = q['surname'].value
        self.year = q['year'].value
        self.citizenship = q['citizenship'].value
        
    def ShowForm(self):
        print(LoadTpl('addFP').format(self.q['student'].value, self.name, self.surname, self.year, self.citizenship))

    def Change(self, q):
        print(LoadTpl('editFP').format(q['student'].value,q['i'].value, self.name, self.surname, self.year, self.citizenship))       

    def Show(self, q, i):
        print(LoadTpl('showFP').format(q['student'].value,i, self.name,  self.surname, self.year, self.citizenship))
  



