import pickle, os
from .sportsman import *
from .employee import *

class Spisok:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q = q
        self.selfurl = selfurl

        
    def read(self):
        self.read_file()
        id = int(self.q['id'].value)
        if (id==len(self.l)): self.l.append(0)
        if ('sport' in self.q):
            self.sport = self.q['sport'].value
        else: self.sport = ""
        if (self.sport==""): self.l[id]=Employee()
        else: self.l[id]=Sportsman()
        self.l[id].read(self.q, self.selfurl)
        self.write_file()
        self.write()
        
    def write(self):
        self.read_file()
        if (len(self.l)!=0):
            i=0
            print('<H3>Сотрудники спортивной команды</H3><table border><tr><td>Фамилия</td><td>Имя</td><td>Возраст</td><td>Пол</td><td>Вид спорта</td><td>Действия</td></tr>')
            for o in self.l:
                o.write()
                if type(o) is Employee: print('<td></td>')
                print('<td><a href="{0}?student={1}&action=1&type=2&id={2}">Редактировать</a> | <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=1&id={2}">Добавить сотрудника команды</a> '.format(self.selfurl, self.q['student'].value, len(self.l)))    

            
            
    def change(self):
        self.read_file()
        id = int(self.q['id'].value)
        if (id==len(self.l)): Sportsman().write_ch(self.q,self.selfurl)
        else: 
            self.l[id].write_ch(self.q,self.selfurl)
            if type(self.l[id]) is Employee: 
                print('<br>Вид спорта:<br><input type="text" name="sport" value=""><br>')
        print('<a href="{0}?student={1}">Отмена   </a><input type="submit" value="Сохранить"></form>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_file()
        id = int(self.q['id'].value)
        self.l.pop(id)
        self.write_file()
        self.write()
            
           
    def read_file(self):
        if (os.path.exists("cgi-bin/st20/file.dat")):
            self.l = pickle.load(open("cgi-bin/st20/file.dat", "rb"))
            
        
    def write_file(self):
            pickle.dump(self.l, open("cgi-bin/st20/file.dat", "wb"))
    

    
