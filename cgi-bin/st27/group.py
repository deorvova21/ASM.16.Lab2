from .Dire import *
from .Radiant  import *
import pickle, os

class group:
    def __init__(self, q, selfurl):
        self.list=[]
        self.q = q
        self.selfurl = selfurl

    def show_all(self):
        self.load()
        if len(self.list) == 0:
            print("Список героев пуст")
        else:
            print("""<table border><Caption><H3>Список героев</H3></Caption>
                  <tr><th colspan="2">Имя и Фракция героя</th><th colspan="5">Основные характеристики героя</th><th rowspan="2">Действие</th></tr> 
                  <tr><th>Имя героя</th><th>Фракция</th>
                  <th>Сила атаки</th><th>Кол-во здоровья</th><th>Ловкость</th><th>Сила</th><th>Интеллект</th></tr>""")
            i = 0
            for item in self.list:
                item.add_to_table()
                print("""<td><a href="{0}?student={1}&action=del&id={2}">Удалить</a> /
                         <a href="{0}?student={1}&action=edit&id={2}">Редактировать</a>
                         </td>""".format(self.selfurl, self.q['student'].value, i))
                print("</tr>")
                i += 1
            print("</table>")
        print("""<br><a href="{0}?student={1}&action=Dadd">Добавить героя фракции Dire</a>
                 <br><a href="{0}?student={1}&action=Radd">Добавить героя фракции Raiant</a>
                 <br><a href="{0}?student={1}&action=clear">Очистить список</a>
                 <br><a href="{0}">Назад</a>
                 """.format(self.selfurl, self.q['student'].value))

    def load(self):
        if (os.path.exists("cgi-bin/st27/Heroes.dat")):
            self.list =  pickle.load(open("cgi-bin/st27/Heroes.dat", "rb"))

    def Dadd(self):
        self.load()
        di = Dire(self.q)
        self.list.append(di)
        di.new()
        di.save_values(self.q)
        if di.hname != "":
            self.save()
            print('<br><th>Герой фракции Dire добавлен</th>')

    def Radd(self):
        self.load()
        rad = Radiant(self.q)
        self.list.append(rad)
        rad.new()
        rad.save_values(self.q)
        if rad.hname != "":
            self.save()
            print('<br><th>Герой фракции Radiant добавлен</th>')

    def save(self):
        pickle.dump(self.list, open('cgi-bin/st27/Heroes.dat', 'wb'))

    def save_item(self):
        self.list.append()
        self.save()
        self.show_all()

    def delete(self):
        self.load()
        self.list.pop(int(self.q['id'].value))
        self.save()
        self.show_all()

    def edit(self):
        self.load()
        self.list[int(self.q['id'].value)].edit(self.q)
        self.list[int(self.q['id'].value)].save_values(self.q)
        self.save()
        print('<br><th>Герой изменен</th>')

    def clear(self):
        self.load()
        self.list.clear()
        self.save()
        self.show_all()
              
