from .employee import Employee

class EmployeeInfo(Employee):
     
    def __init__(self):
        Employee.__init__(self)
        self.salary = ""
        self.age = ""

    def form(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table cellpadding="7" border="1"><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Фамилия:')
        print('<input type = "text" name = "surname" value="{0}">'.format(self.surname))
        print('Имя:')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Должность:')
        print('<input type = "text" name = "position" value="{0}">'.format(self.position))
        print('ЗП:')
        print('<input type = "text" name = "salary" value="{0}">'.format(self.salary))
        print('Возраст:')
        print('<input type = "text" name = "age" value="{0}">'.format(self.age))
        print('<input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "7" >')
        print('</form></tr></td></table>')

    def read(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        #Employee.read(self)
        self.surname=self.q['surname'].value
        self.name = self.q['name'].value
        self.position = self.q['position'].value
        self.salary = self.q['salary'].value
        self.age = self.q['age'].value

    def show(self):
        print("<br>Фамилия: {0} | Имя: {1} | Должность: {2} | ЗП: {3} | Возраст: {4}".format(self.surname, self.name, self.position, self.salary, self.age))