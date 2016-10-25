import pickle, os
from .student import *
from .mayor import *

class Group:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q = q
        self.selfurl = selfurl
        
    def read(self):
        self.read_file()
        id = int(self.q['id'].value)
        self.l[id].read(self.q, self.selfurl)
        self.write_file()
        self.write()

        
    def write(self):
        self.read_file()
        k=-1
        if (len(self.l)!=0):
            if 'type' in self.q:
                if (self.q['type'].value=="2"):
                    k=int(self.q['id'].value)
            print('<H3>Учебная группа</H3><table border><tr><td>Имя</td><td>Пол</td><td>Возраст</td><td>Размер стипендии</td><td>Телефон</td><td>Действия</td></tr>')
            i=0
            for o in self.l:
                if (i!=k):
                    o.write()
                else:
                    o.write_ch(self.q, self.selfurl)
                if type(o) is Student: print('<td>Не староста</td>')
                print('<td><a href="{0}?student={1}&action=1&type=2&id={2}">Редактировать</a> | <a href="{0}?student={1}&action=4&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        if (k==-1):
            print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=3&stype=1">Добавить студента </a> | <a href="{0}?student={1}&action=3&stype=2">Добавить старосту </a>'.format(self.selfurl, self.q['student'].value))
        else:
            print('<a href="{0}?student={1}">Отмена   </a><input type="submit" value="Сохранить"></form>'.format(self.selfurl, self.q['student'].value))    

    def add(self):
        self.read_file()
        if (self.q['stype'].value=="1"): self.l.append(Student())
        if (self.q['stype'].value=="2"): self.l.append(Mayor())
        self.write_file()
        self.write()

    def cd(self,i):
        self.write()
        if (len(self.l)==0): return
        print("Для изменения выберите номер элемента в списке")
        print("Для возврата в предыдуще меню нажмите 0")
        try:
            m = int(input())
            if (m==0): return
            if (i==1):    
                self.l[m-1].read()
                print("Изменено!")
            if (i==2):
                self.l.pop(m-1)
                print("Удалено!")
        except:
            print("Введено некорректное значение")
            self.cd(i)                

    def delete(self):
        self.read_file()
        id = int(self.q['id'].value)
        self.l.pop(id)
        self.write_file()
        self.write()
       
    def read_file(self):
        if (os.path.exists("cgi-bin/st06/list.dat")):
            self.l = pickle.load(open("cgi-bin/st06/list.dat", "rb"))
     
    def write_file(self):
            pickle.dump(self.l, open("cgi-bin/st06/list.dat", "wb"))
    
