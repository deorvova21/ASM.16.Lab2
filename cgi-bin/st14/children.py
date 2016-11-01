import cgi
class Children:
    def __init__(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        self.name=""
        self.sername=""
        self.age=""
        self.group_number=""

        
    def read(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("Имя",":")
        if ('Имя' in self.q):
            self.name = self.q['Имя'].value
        else: self.name=""
        if ('Фамилия' in self.q):
            self.sername = self.q['Фамилия'].value
        else: self.sername = ""
        if ('Возраст' in self.q):
            self.age = self.q['Возраст'].value
        else: self.age = ""
        if ('Номер группы' in self.q):
            self.group_number = self.q['Номер группы'].value
        else: self.group_number = ""
      
        
    def write_ch(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}"style="display:none" >'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}"style="display:none" >'.format("1"))
        print('<input type="text" name="type" value="{0}"style="display:none" >'.format("3"))
        print('<input type="text" name="id" value="{0}"style="display:none" >'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}"style="display:none" >'.format(self.q['type'].value))
        print('Имя<br><input type="text" name="Имя" value="{0}">'.format(self.name))
        print('<br>Фамилия<br><input type="text" name="Фамилия" value="{0}">'.format(self.sername))
        print('<br>Возраст<br><input type="text" name="Возраст" value="{0}">'.format(self.age))
        print('<br>Номер группы<br><input type="text" name="Номер группы" value="{0}">'.format(self.group_number))
        

    def write(self):
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.sername))
        print('<td>{0}</td>'.format(self.age))
        print('<td>{0}</td>'.format(self.group_number))
 
