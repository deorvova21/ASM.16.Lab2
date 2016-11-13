import cgi
from .student import *
class Starosta(Student):
        def __init__(self,q):
                super().__init__(q)
                self.phone='' 
        def EditPerson(self,q):
                super().EditPerson(q)
                self.phone=q['phone'].value
                
        def AddPersonForm(self):
                print("""<form>
        <input type=hidden name=type value="AddStar">
        Имя: <input type=text name=name value="{0}"><br>
        Возраст: <input type=text name=age value="{1}"><br>
        Город: <input type=text name=city value="{2}"><br>
        Средний балл: <input type=text name=avg value="{3}"><br>
        Телефон: <input type=text name=phone value="{4}">
        <input type=hidden name=student value="{5}">
        <br>
        <input type=submit value="Добавить">
        </form>""".format (self.name, self.age, self.city,self.avg,self.phone,self.q['student'].value))
            
        def EditForm(self,q):
                print("""<form>
<input type=hidden name=type value="Edit">
Имя: <input type=text name=name value="{0}"><br>
Возраст: <input type=text name=age value="{1}"><br>
Город: <input type=text name=city value="{2}"><br>
Средний балл: <input type=text name=avg value="{3}"><br>
Телефон: <input type=text name=phone value="{4}"><br>
<input type=hidden name=iid value="{5}">
<input type=hidden name=student value="{6}">
<br>
<input type=submit value="Изменить">
</form>""".format (self.name, self.age, self.city,self.avg,self.phone,q['iid'].value,q['student'].value))

        def WritePerson(self,iid):
                print("""<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td>
<td><a href="?student={5}&type=EditForm&iid={6}">Редактировать</a>
<a href="?student={5}&type=Delete&iid={6}">Удалить</a></td></tr>""".format(self.name, self.age, self.city, self.avg,self.phone, self.q['student'].value,iid))   
