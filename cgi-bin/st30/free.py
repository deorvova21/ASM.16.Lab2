import cgi

class Free:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.line = ''
        
    def Write(self):
        print('<b>Свободный агент</b> <br>')
        print('ФИО: {}<br> Возраст: {}<br> Амплуа: {}<br>'.format(self.name, self.age, self.line))

    def ShowEdit(self):
        print('<tr><td>ФИО:</td><td><input type="text" name="name" value="{0}"></td><tr>'.format(self.name))
        print('<tr><td>Возраст:</td><td><input type="text" name="age" value="{0}"></td></tr>'.format(self.age))
        print('<tr><td>Амплуа:</td><td><input type="text" name="line" value="{0}"></td></tr>'.format(self.line))
        
    def SaveEdit(self, q):
        self.name = q.getvalue('name')
        self.age = q.getvalue('age')
        self.line = q.getvalue('line')
