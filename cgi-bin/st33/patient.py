import cgi

class Patient:
    def __init__(self):
        self.name = ''
        self.age = ''
        self.symptoms = ''
        
    def Write(self):
        print('<b>Пациент</b> <br>')
        print('ФИО: {}<br> Возраст: {}<br> Симптоматика: {}<br>'.format(self.name, self.age, self.symptoms))

    def ShowEdit(self):
        print('<tr><td>ФИО:</td><td><input type="text" name="name" value="{0}"></td><tr>'.format(self.name))
        print('<tr><td>Возраст:</td><td><input type="text" name="age" value="{0}"></td></tr>'.format(self.age))
        print('<tr><td>Симптоматика:</td><td><input type="text" name="symptoms" value="{0}"></td></tr>'.format(self.symptoms))
        
    def SaveEdit(self, q):
        self.name = q.getvalue('name')
        self.age = q.getvalue('age')
        self.symptoms = q.getvalue('symptoms')
