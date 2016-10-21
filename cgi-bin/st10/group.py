from .bakalavr import *
from .magistr  import *
import pickle, os

class group:
    def __init__(self, q, selfurl):
        self.list=[]
        self.q = q
        self.selfurl = selfurl

    def show_all(self):
        self.load()
        if len(self.list) == 0:
            print("Список студентов пуст")
        else:
            print("""<table border><Caption><H3>Список студентов</H3></Caption>
                  <tr><th colspan="4">Текущее образование</th><th colspan="3">Предыдущее образование (для магистров)</th><th rowspan="2">Действие</th></tr> 
                  <tr><th>ФИО студента</th><th>Факультет</th><th>Курс</th><th>Группа</th>
                  <th>ВУЗ</th><th>Направление</th><th>Средний балл</th></tr>""")
            i = 0
            for item in self.list:
                item.add_to_table()
                print("""<td><a href="{0}?student={1}&action=del&id={2}">Удалить</a> /
                         <a href="{0}?student={1}&action=edit&id={2}">Редактировать</a>
                         </td>""".format(self.selfurl, self.q['student'].value, i))
                print("</tr>")
                i += 1
            print("</table>")
        print("""<br><a href="{0}?student={1}&action=badd">Добавить бакалавра</a>
                 <br><a href="{0}?student={1}&action=madd">Добавить магистра</a>
                 <br><a href="{0}?student={1}&action=clear">Очистить список</a>
                 <br><a href="{0}">Назад</a>
                 """.format(self.selfurl, self.q['student'].value))

    def load(self):
        if (os.path.exists("cgi-bin/st10/students.dat")):
            self.list =  pickle.load(open("cgi-bin/st10/students.dat", "rb"))

    def badd(self):
        self.load()
        bak = bakalavr(self.q)
        self.list.append(bak)
        bak.new()
        bak.save_values(self.q)
        if bak.fio != "":
            self.save()
            print('<br><th>Бакалавр добавлен</th>')

    def madd(self):
        self.load()
        mag = magistr(self.q)
        self.list.append(mag)
        mag.new()
        mag.save_values(self.q)
        if mag.fio != "":
            self.save()
            print('<br><th>Магистр добавлен</th>')

    def save(self):
        pickle.dump(self.list, open('cgi-bin/st10/students.dat', 'wb'))

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
        print('<br><th>Студент изменен</th>')

    def clear(self):
        self.load()
        self.list.clear()
        self.save()
        self.show_all()
              
