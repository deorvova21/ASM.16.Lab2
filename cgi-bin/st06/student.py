class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""
        self.age = ""
        self.grants = ""      
        
    def read(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name=""
        if ('sex' in self.q):
            self.sex = self.q['sex'].value
        else: self.sex = ""
        if ('age' in self.q):
            self.age = self.q['age'].value
        else: self.age = ""
        if ('grants' in self.q):
            self.grants = self.q['grants'].value
        else: self.grants = ""
        
    def write(self):
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.sex))
        print('<td>{0}</td>'.format(self.age))
        print('<td>{0}</td>'.format(self.grants))

    def write_ch(self, q, selfurl):
        self.selfurl=selfurl
        self.q=q
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("2"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<td><input type="text" name="name" value="{0}"></td>'.format(self.name))
        print('<td><input type="text" name="sex" value="{0}"></td>'.format(self.sex))
        print('<td><input type="text" name="age" value="{0}"></td>'.format(self.age))
        print('<td><input type="text" name="grants" value="{0}"></td>'.format(self.grants))
