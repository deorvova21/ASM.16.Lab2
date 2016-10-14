import os,re,sys,cgi,pickle
from .Starosta import *

class University:
    def __init__(self,q,selfurl):
        self.q=q
        self.spisok=[]
        self.amount=len(self.spisok)
        self.selfurl=selfurl
        
    def new_stu(self):
        self.load()
        student=Student(self.q)
        self.spisok.append(student)
        student.write()
        student.edit(self.q)
        self.store()
        print('<br>студент добавлен\n<br>')
        
              
    def new_sta(self):
        self.load()
        starosta=Starosta(self.q)
        self.spisok.append(starosta)
        starosta.write()
        starosta.edit(self.q)
        self.store()
        print('староста добавлена\n<br>')
        
        
    def edit(self):
        self.load()
        self.spisok[int(self.q['i'].value)].edit(self.q)
        self.store()
        self.ShowSpisok()
        
    def load(self): # чтение файла
        if (os.path.exists('cgi-bin/st24/university.db')):
            with open('cgi-bin/st24/university.db', 'rb') as f:
                self.spisok = pickle.load(f)
            
    def change(self):
    
        self.load()
        item=self.spisok[int(self.q['i'].value)]
        item.change(self.q)       
        
        
        
    def dell(self):
        self.load()
        self.spisok.pop(int(self.q['i'].value))
        self.store()
        self.ShowSpisok()
        
    def dell_all(self):
        self.load()
        self.spisok.clear()
        self.store()
        self.ShowSpisok()
                
    def store(self): # запись файла
        with open('cgi-bin/st24/university.db', 'wb') as f:
            pickle.dump(self.spisok, f)
            
    def ShowSpisok(self):
        self.load()
        print('Всего : ---'+str(len(self.spisok))+' учащихся\n<br><hr>')
        i=0
        for item in self.spisok:
            item.show(i)
            i+=1
        print("""
<a href="?student={0}&type=add_sta">Добавить старосту</a> | <a href="?student={0}&type=add_stu">Добавить студента</a>
| <a href="?student={0}&type=dell_all">Удалить всех</a><br> <a href="{1}">Назад</a>
""".format(self.q['student'].value, self.selfurl))
    
