import cgi

class Student:
    def __init__(self,q):
        self.name=''
        self.q=q
        self.group=''
        self.mark=''
        
    def edit(self,q):
        self.name = q['name'].value
        self.group = q['group'].value
        self.mark = q['mark'].value
        
    def write(self):
        print("""
<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="add_stu">
Имя: <input type=text name=name value="{1}"><br>
Группа: <input type=text name=group value="{2}"><br>
Средний балл: <input type=text name=mark value="{3}"><br>
<br>
<input type=submit value="Ввод">
</form>
<a href="?student={0}">Назад</a>
        """.format(self.q['student'].value, self.name, self.group,self.mark))

    def change(self, q):
        print("""
<form>
<input type=hidden name=student value="{0}">
<input type=hidden name=type value="edit">
<input type=hidden name=i value="{1}">
Имя: <input type=text name=name value="{2}"><br>
Группа: <input type=text name=group value="{3}"><br>
Средний балл: <input type=text name=mark value="{4}"><br>
<br>
<input type=submit value="Ввод">
<br>
</form>
<a href="?student={0}">Назад</a>
        """.format(q['student'].value,q['i'].value, self.name, self.group,self.mark))       

    def show(self, i):
        print("""
Имя: {2}<br>
Группа: {3}<br>
Средний балл: {4}<br>
<a href="?student={0}&type=change&i={1}">Редактировать</a> | <a href="?student={0}&type=dell&i={1}">Удалить</a><br>
<hr>
""".format(self.q['student'].value,i, self.name,self.group,self.mark))
  




    
    
