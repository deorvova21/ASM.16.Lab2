class Employee(object):
    def __init__(self):
        self.surname = ""
        self.name = ""
        self.position = ""

    def form(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        print('<br><table cellpadding="7" border="1"><tr><td>')
        print('<form action="{0}" method="get">'.format(self.selfurl))
        print('<input type="hidden" name = "index" value = "{0}" >'.format(self.q['index'].value))
        print('<input type="hidden" name = "student" value = "{0}" >'.format(self.q['student'].value))
        print('<br> Фамилия: ')
        print('<input type = "text" name = "surname" value="{0}">'.format(self.surname))
        print('Имя:')
        print('<input type = "text" name = "name" value="{0}">'.format(self.name))
        print('Должность: ')
        print('<input type = "text" name = "position" value="{0}">'.format(self.position))
        print('<input type = "submit" value = "Применить">')
        print('<input type="hidden" name = "action" value = "6" >')
        print('</form></tr></td></table>')

    def read(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self.surname=self.q['surname'].value
        self.name = self.q['name'].value
        self.position = self.q['position'].value

    def show(self):
        print("<br><br>Фамилия: {0} | Имя: {1} | Должность: {2}".format(self.surname,self.name,self.position))
