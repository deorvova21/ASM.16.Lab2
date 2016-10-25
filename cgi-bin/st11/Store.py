import os,pickle,copy 
from .Phone import *
from .Smartphone import *

class Store:
    def __init__(self, q, selfurl):
        self.List=list()
        self.q = q
        self.selfurl = selfurl

    def new_(self):
        self.load_file()
        if ('type' in self.q):       
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"):
                    Phone(self.q, self.selfurl).show_form()
                if (self.q['type'].value=="2"):
                    Smartphone(self.q, self.selfurl).show_form()
                if (self.q['type'].value=="5"):
                    self.List[int(self.q['id'].value)].show_form()
                print('<table>')
                print('<td align="right" width="100"></td><td><input type="submit" value="Сохранить"></td></tr>')
                print('</table>')
                print('</form>')
            else:
                if (len(self.List)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"):
                        self.List.append(Phone(self.q, self.selfurl))
                    if (self.q['add'].value=="2"):
                        self.List.append(Smartphone(self.q, self.selfurl))
                self.List[int(self.q['id'].value)].read()
                self.save_file()
                self.print_()
        else:
            k=len(self.List)
            print('<a href="{0}?student={1}&selection=1&type=1&id={2}">Добавить телефон</a><br><a href="{0}?student={1}&selection=1&type=2&id={2}">Добавить смартфон</a>'.format(self.selfurl, self.q['student'].value, k))

    def delete(self):
        self.load_file()
        self.List.pop(int(self.q['id'].value))
        self.save_file()
        self.print_()

    def print_(self):
        self.load_file()
        print('<title>[11] Гюльназарян</title>')
        print('<style>th { background: #afd792; color: #333; font-family: Arial}</style><table border cellspacing="0"><tr align="center"><th>Марка</th><th>Модель</th><th>Кол-во</th><th>Цена</th><th>ОС</th><th>Версия ОС</th><th></th></th>')
        if (len(self.List)!=0):
            i=0
            for n in self.List:
                print('<style>tbody tr:hover {background: #f3bd48;color: #fff}</style><tbody><tr height="20">')
                n.show_values()
                if type(n) is Phone:
                    print('<td>-</td>')
                    print('<td>-</td>')
                print('<td><a href="{0}?student={1}&selection=1&type=5&id={2}">Изменить</a> // <a href="{0}?student={1}&selection=3&id={2}">X</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr></tbody>')
                i+=1
            print('</table>')
            print('<br><a href="{0}">←</a>'.format(self.selfurl, self.q['student'].value))   
            print('<br><a href="{0}?student={1}&selection=1">Добавить товар</a>'.format(self.selfurl, self.q['student'].value))
            print('<br><a href="{0}?student={1}&selection=4">Удалить все</a>'.format(self.selfurl, self.q['student'].value))
        else:
            print('<br><a href="{0}">←</a><br><a href="{0}?student={1}&selection=1">Добавить товар</a>'.format(self.selfurl, self.q['student'].value))

    def clear(self):
        self.load_file()
        self.List.clear()
        self.save_file()
        self.print_()

    def save_file(self):
        pickle.dump(self.List, open("cgi-bin/st11/11.txt", "wb"))            
       
    def load_file(self):
        if (os.path.exists("cgi-bin/st11/11.txt")):
            self.List = pickle.load(open("cgi-bin/st11/11.txt", "rb"))

