import cgi

class Student:
    def __init__(self):
        self.name=''
        self.dob=''
        self.group=''

    def print_me(self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>'.format(self.name, self.dob, self.group, '-'))

    def show_edit(self):
        print('<tr><td>Имя:</td><td><input type="text" name="name" value="{0}"></td><tr>'.format(self.name))
        print('<tr><td>Дата рождения:</td><td><input type="text" name="dob" value="{0}"></td></tr>'.format(self.dob))
        print('<tr><td>Группа:</td><td><input type="text" name="group" value="{0}"></td></tr>'.format(self.group))

    def edit_me(self, q):
        self.name = q.getvalue('name')
        self.dob = q.getvalue('dob')
        self.group = q.getvalue('group')
