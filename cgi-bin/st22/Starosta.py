import cgi
from .Student import *

class Starosta(Student):
    def __init__(self,q):
        super().__init__(q)
        self.age=age=""
        self.salary=salary=""
        self.q=self.q
        
    def edit(self,q):
        self.name = q['name'].value
        self.group = q['group'].value
        self.mark = q['mark'].value
        self.age = q['age'].value
        self.salary = q['salary'].value
        
    def write(self):
        print("""
<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="add_sta">
Имя старосты: <input type=text name=name value="{1}"><br>
Группа старосты: <input type=text name=group value="{2}"><br>
Средний балл старосты: <input type=text name=mark value="{3}"><br>
Возраст старосты: <input type=text name=age value="{4}"><br>
Зарплата старосты: <input type=text name=salary value="{5}"><br>
<br>
<input type=submit value="Ok">
<br>
<a href="?student={0}">Назад</a>
</form>
        """.format(self.q['student'].value, self.name,self.group, self.mark, self.age, self.salary))

    def change(self,q):
        print("""
<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="edit">
<input type=hidden name=i value="{1}">
Имя старосты: <input type=text name=name value="{2}"><br>
Группа старосты: <input type=text name=group value="{3}"><br>
Средний балл старосты: <input type=text name=mark value="{4}"><br>
Возраст старосты: <input type=text name=age value="{5}"><br>
Зарплата старосты: <input type=text name=salary value="{6}"><br>
<br>
<input type=submit value="Ok">
<br>
</form>
<a href="?student={0}">Назад</a>
        """.format(q['student'].value, q['i'].value, self.name,self.group, self.mark, self.age, self.salary))

    def show(self, q, i):
        print("""
вы ввели старосту: <br>
Имя: {2}<br>
Группа: {3}<br>
Средний балл: {4}<br>
Возраст старосты: {5}<br>
Зарплата: {6}<br> 
<a href="?student={0}&type=change&i={1}">Редактировать</a> | <a href="?student={0}&type=dell&i={1}">Удалить</a><br>
<hr>
""".format(q['student'].value, i, self.name, self.group, self.mark, self.age, self.salary))


