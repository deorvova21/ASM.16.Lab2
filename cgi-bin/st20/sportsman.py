from .employee import *

class Sportsman(Employee):
    def __init__(self):
        super().__init__()
        self.sport =""

    def read(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        Employee.read(self, self.q, self.selfurl)
        if ('sport' in self.q):
            self.sport = self.q['sport'].value
        else: self.sport = ""


    def write(self):
        Employee.write(self)
        print('<td>{0}</td>'.format(self.sport))

    def write_ch(self, q, selfurl):
        Employee.write_ch(self, q, selfurl)
        print('<br>Вид спорта:<br><input type="text" name="sport" value="{0}"><br>'.format(self.sport))