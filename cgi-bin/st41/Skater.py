import cgi
from .LoadTpl import *

class Skater:
    def __init__(self, q):
        self.name=''
        self.q=q
        self.discipline=''
                
    def edit(self, q):
        self.name = q['name'].value
        self.discipline = q['discipline'].value
                
    def showform(self):
        print(LoadTpl('add_skater').format(self.q['student'].value, self.name, self.discipline))
        
    def change(self, q):
        print(LoadTpl('edit_skater').format(q['student'].value,q['i'].value, self.name, self.discipline))
            

    def show(self, q, i):
        print(LoadTpl('show_skater').format(q['student'].value,i, self.name, self.discipline))



    
    
