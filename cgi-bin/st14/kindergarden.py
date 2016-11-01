import pickle, copy, os
from .children import Children
from .wonderkind import Wonderkind

class Kindergarden:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q = q
        self.selfurl = selfurl

    def read(self):
        self.read_f()
        if ('type' in self.q):       
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"): Children(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="2"): Wonderkind(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="4"): self.l[int(self.q['id'].value)].write_ch()
                print('<br><br><input type="submit" value="Готово!">')
                print('</form>')
            else:
                if (len(self.l)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"): self.l.append(Children(self.q, self.selfurl))
                    if (self.q['add'].value=="2"): self.l.append(Wonderkind(self.q, self.selfurl))
                self.l[int(self.q['id'].value)].read()
                self.write_f()
                self.write()
        else:
            k=len(self.l)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">Обычный</a> / <a href="{0}?student={1}&action=1&type=2&id={2}">Вундеркинд</a>'.format(self.selfurl, self.q['student'].value, k))

    def write(self):
        self.read_f()
        if (len(self.l)!=0):
            print('<table border><Caption><H2>Десткий садик "Радость"</H2></Caption><tr><td>Имя</td><td>Фамилия</td><td>Возраст</td><td>Номер группы</td><td>Особенность</td><td>Что сделать?</td></tr>')
            i=0
            for o in self.l:
                print('<tr height="30">')
                o.write()
                if type(o) is Children: print('<td>Отсутствует</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Изменить</a> / <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Вернуться</a> / <a href="{0}?student={1}&action=1">Добавить ребенка</a>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_f()
        self.l.pop(int(self.q['id'].value))
        self.write_f()
        self.write()       
            
       
    def read_f(self):
        if (os.path.exists("cgi-bin/st14/file.dat")):
            self.l = pickle.load(open("cgi-bin/st14/file.dat", "rb"))

    def write_f(self):
        pickle.dump(self.l, open("cgi-bin/st14/file.dat", "wb"))
