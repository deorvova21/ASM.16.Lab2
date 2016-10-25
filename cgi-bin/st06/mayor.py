from .student import *

class Mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
    
    def read(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        Student.read(self, self.q, self.selfurl)
        if ('telephone' in self.q):
            self.telephone = self.q['telephone'].value
        else: self.telephone = ""

    def write(self):
        Student.write(self)
        print('<td>{0}</td>'.format(self.telephone))

    def write_ch(self, q, selfurl):
        Student.write_ch(self, q, selfurl)
        print('<td><input type="text" name="telephone" value="{0}"></td>'.format(self.telephone))
    
    
