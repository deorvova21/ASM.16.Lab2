import pickle, copy, os
from .products import Products
from .vegetables import Vegetables
from .fruits import Fruits

class Group:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q=q
        self.selfurl=selfurl

    def read(self):
        self.read_file()
        if (len(self.l)==int(self.q['id'].value)):
            if (self.q['add'].value=="1"): self.l.append(Vegetables(self.q, self.selfurl))
            if (self.q['add'].value=="2"): self.l.append(Fruits(self.q, self.selfurl))
        self.l[int(self.q['id'].value)].read(self.q)
        self.write_file()
        self.write()

    def write_ch(self):
        self.read_file()
        if (self.q['type'].value=="1"): Vegetables(self.q, self.selfurl).write_ch(self.q)
        if (self.q['type'].value=="2"): Fruits(self.q, self.selfurl).write_ch(self.q)
        if (self.q['type'].value=="4"): self.l[int(self.q['id'].value)].write_ch(self.q)
        print('<br><br><br></table><input type="submit" value="Сохранить">')
        print('</form>')

    def add(self):
        self.read_file()
        k=len(self.l)
        print('<td><a href="{0}?student={1}&action=4&type=1&id={2}">Овощи</a> | <a href="{0}?student={1}&action=4&type=2&id={2}">Фрукты</a></td>'.format(self.selfurl, self.q['student'].value, k))


    def write(self):
        self.read_file()
        if (len(self.l)!=0):
            i=0
            for o in self.l:
                print('<tr height="20">')
                o.write()
                print('<td><a href="{0}?student={1}&action=4&type=4&id={2}">Редактировать</a> | <a href="{0}?student={1}&action=3&id={2}">Удалить</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
                print('</table>')
        print('<br><br><a href="{0}">Назад</a> | <a href="{0}?student={1}&action=5">Добавить продукты</a>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_file()
        self.l.pop(int(self.q['id'].value))
        self.write_file()
        self.write()       
               
    def read_file(self):
        if (os.path.exists("cgi-bin/st03/file.txt")):
            self.l = pickle.load(open("cgi-bin/st03/file.txt", "rb"))

    def write_file(self):
        pickle.dump(self.l, open("cgi-bin/st03/file.txt", "wb"))
    

    
