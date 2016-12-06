import pickle, cgi, os
from .class2 import *

class container:
    def __init__(self, q, selfurl):
        self.data = []
        self.q = q
        self.selfurl = selfurl

    def addClass1(self):
        self.readFile()
        сlass1 = class1()
        self.data.append(сlass1)
        self.writeFile()
        self.editObj()

    def addClass2(self):
        self.readFile()
        сlass2 = class2()
        self.data.append(сlass2)
        self.writeFile()
        self.editObj()

    def showList(self):
        self.readFile()
        print('<table><tr><th>Поле 1</th><th>Поле 2</th><th>Поле 3</th><th>Поле 4</th><th>Редактировать / Удалить</th></tr>')
        i = 0
        for item in self.data:
            print('<tr>')
            item.write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=deleteObj&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            i+=1
        print('<table>')
        print('<input type="hidden" name="student" value={0} />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" id="act" value="showList" />')
        print('<br>')
        print('<a href={0}>Назад</a>'.format(self.selfurl))
        print('<p><a href={0}?student={1}&act=addClass1>Добавить объект класса 1</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=addClass2>Добавить объект класса 2</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clearList>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))

    def writeFile(self):
        pickle.dump(self.data, open('file.dat', 'wb'))
        print("Файл записан")

    def readFile(self):
        self.data = pickle.load(open('file.dat', 'rb'))
        print ("Файл считан")

    def clearList(self):
        self.readFile()
        self.data.clear()
        self.writeFile()
        self.showList()

    def deleteObj(self):
        self.readFile()
        self.data.pop(int(self.q['id'].value))
        self.writeFile()
        self.showList()

    def get(self):
        self.readFile()
        self.data[int(self.q['id'].value)].edit(self.q)
        self.writeFile()
        self.showList()
            
    def editObj(self):
        self.readFile()
        print('<title>Изменение данных</title>\n<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        idObj = str()
        if 'id' in self.q:
            idObj = self.q.getvalue('id')
        else:
            idObj = str(len(self.data)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(idObj))
        print('<table>')
        self.data[int(idObj)].show()
        print('</table>')
        print('<input type="submit" value="Сохранить">')

    def readFile(self):
        self.data = pickle.load(open('cgi-bin/st26/file.dat', 'rb'))

    def writeFile(self):
        pickle.dump(self.data, open('cgi-bin/st26/file.dat', 'wb'))

    def edit(self):
        pickle.dump(self.data, open('cgi-bin/st26/file.dat', 'wb'))
