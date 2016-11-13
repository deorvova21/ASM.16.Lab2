import cgi
class Student:
        def __init__(self, q):              
            self.name = ''
            self.age = ''
            self.city = ''
            self.avg= ''
            self.q=q
        def EditPerson(self,q):
                self.name=q['name'].value
                self.age=q['age'].value
                self.city=q['city'].value
                self.avg=q['avg'].value
        def AddPersonForm(self):
                print("""<form>
<input type=hidden name=type value="AddStud">
Имя: <input type=text name=name value="{0}"><br>
Возраст: <input type=text name=age value="{1}"><br>
Город: <input type=text name=city value="{2}"><br>
Средний балл: <input type=text name=avg value="{3}"><br>
<input type=hidden name=student value="{4}">
<br>
<input type=submit value="Добавить">
<a href="?student={4}">Назад</a>
</form>""".format (self.name, self.age, self.city,self.avg,self.q['student'].value))
        def EditForm(self, q):
                print("""<form>
<input type=hidden name=type value="Edit">
Имя: <input type=text name=name value="{0}"><br>
Возраст: <input type=text name=age value="{1}"><br>
Город: <input type=text name=city value="{2}"><br>
Средний балл: <input type=text name=avg value="{3}"><br>
<input type=hidden name=iid value="{4}">
<input type=hidden name=student value="{5}">
<br>
<input type=submit value="Изменить">
</form>""".format (self.name, self.age, self.city,self.avg,q['iid'].value,q['student'].value))

        def WritePerson(self,iid):
                   print("""<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td></td>
<td><a href="?student={4}&type=EditForm&iid={5}">Редактировать</a>
<a href="?student={4}&type=Delete&iid={5}">Удалить</a></tr>""".format(self.name, self.age, self.city, self.avg,self.q['student'].value,iid))       
        



















                
        
        



    
            
