class Employee:
    def __init__(self):
        self.surname=""
        self.name = ""
        self.age = ""
        self.sex = ""
        
    def read(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        if ('surname' in self.q):
            self.surname = self.q['surname'].value
        else: self.surname=""
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name = ""
        if ('age' in self.q):
            self.age = self.q['age'].value
        else: self.age = ""
        if ('sex' in self.q):
            self.sex = self.q['sex'].value
        else: self.sex = ""

    def write(self):
        print('<td>{0}</td>'.format(self.surname))
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.age))
        print('<td>{0}</td>'.format(self.sex))

    def write_ch(self, q, selfurl):
        self.selfurl=selfurl
        self.q=q
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("2"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<br>Фамилия<br><input type="text" name="surname" value="{0}">'.format(self.surname))
        print('<br>Имя<br><input type="text" name="name" value="{0}">'.format(self.name))
        print('<br>Возраст<br><input type="text" name="age" value="{0}">'.format(self.age))
        print('<br>Пол<br><input type="text" name="sex" value="{0}">'.format(self.sex))