import pickle, cgi, os
from .celder import *

class List:
    def __init__(self, q, selfurl):
        self.students = []
        self.q = q
        self.selfurl = selfurl

    def print_script(self):
        print('<script>')
        print(' function ChangeValue(act,id){')
        print('  document.getElementById(\'act\').value = act;')
        print('  document.getElementById(\'id\').value = id;\n }')
        print('</script>')

    def add_student(self):
        self.load()
        student = Student()
        self.students.append(student)
        self.save()
        self.edit()

    def add_elder(self):
        self.load()
        elder = Elder()
        self.students.append(elder)
        self.save()
        self.edit()

    def display(self):
        self.load()
        print('<title>Ягелло</title>\n<form>')
        self.print_script()
        print('<table border cellspacing="0"><tr align="center"><td>Имя</td><td>Дата рождения</td><td>Группа</td><td>Надбавка к стипендии</td><td>Опции</td></tr>')
        i = 0
        for item in self.students:
            print('<tr>')
            item.print_me()
            print('<td><input type="submit" onclick="ChangeValue(\'edit\',\'{0}\')" value ="Редактировать"><input type="submit" onclick="ChangeValue(\'delete\',\'{0}\')" value="Удалить"></td></tr>'.format(i))
            i+=1
        print('</table>')
        print('<input type="hidden" name="student" value={0} />'.format(self.q['student'].value))
        print('<input type="hidden" name="act" id="act" value="display" />')
        print('<input type="hidden" name="id" id="id" value="0" />')
        print('<p><input type="submit" onclick="ChangeValue(\'addstudent\',\'{0}\')" value="Добавить студента">'.format(len(self.students)))
        print('<input type="submit" onclick="ChangeValue(\'addelder\',\'{0}\')" value="Добавить старосту">'.format(len(self.students)))
        print('<p><input type="submit" onclick="ChangeValue(\'clear\',\'\')" value="Очистить список">')
        print('<p><button type="button" onclick="location.href=\'{0}\'">Назад</button>'.format(self.selfurl))
        print('</form>')

    def get(self):
        self.load()
        self.students[int(self.q['id'].value)].edit_me(self.q)
        self.save()
        self.display()

    def edit(self):
        self.load()
        print('<title>Ягелло</title>\n<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q['student'].value))
        print('<input type="hidden" name="act" id="act" value="get" />')
        print('<input type="hidden" name="id" id="id" value="{0}" />'.format(self.q['id'].value))
        print('<table>')
        self.students[int(self.q['id'].value)].show_edit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def save(self):
        pickle.dump(self.students, open('cgi-bin/st40/list.bin', 'wb'))

    def load(self):
        if (os.path.exists('cgi-bin/st40/list.bin')):
            self.students = pickle.load(open('cgi-bin/st40/list.bin', 'rb'))

    def delete(self):
        self.load()
        self.students.pop(int(self.q['id'].value))
        self.save()
        self.display()

    def clear(self):
        self.load()
        self.students.clear()
        self.save()
        self.display()

