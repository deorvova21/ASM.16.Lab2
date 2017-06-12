import cgi
from .FootballPlayer import *
from .LoadTpl import *

class ProfessionalFootballPlayer(FootballPlayer):
    def __init__(self,q):
        super().__init__(q)
        self.salary=''
        self.contract=''
        
        
    def Edit(self,q):
        self.name = q['name'].value
        self.surname = q['surname'].value
        self.year = q['year'].value
        self.citizenship = q['citizenship'].value
        self.salary=q['salary'].value
        self.contract=q['contract'].value
        
    def ShowForm(self):
        print(LoadTpl('addPFP').format(self.q['student'].value, self.name, self.surname, self.year, self.citizenship, self.salary, self.contract))

    def Change(self,q):
        print(LoadTpl('editPFP').format(q['student'].value, q['i'].value, self.name, self.surname, self.year, self.citizenship, self.salary, self.contract))

    def Show(self, q, i):
        print(LoadTpl('showPFP').format(q['student'].value, i, self.name, self.surname, self.year, self.citizenship, self.salary, self.contract))


