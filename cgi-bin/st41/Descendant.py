import cgi
from .Skater import *
from .LoadTpl import *

class Descendant(Skater):
    def __init__(self, q):
        super().__init__(q)
        self.coach=coach=""
        self.q=self.q
        
    def edit(self, q):
        self.name = q['name'].value
        self.discipline = q['discipline'].value
        self.coach = q['coach'].value
                
    def showform(self):
        print(LoadTpl('add_descendant').format(self.q['student'].value, self.name, self.discipline, self.coach))
        
    def change(self, q):
        print(LoadTpl('edit_descendant').format(q['student'].value, q['i'].value, self.name, self.discipline, self.coach))
        
    def show(self, q, i):
        print(LoadTpl('show_descendant').format(q['student'].value, i, self.name, self.discipline, self.coach))        


