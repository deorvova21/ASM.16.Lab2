from .free import *

class Contract(Free):
    def __init__(self):
        super().__init__()
        self.team = ''
        
    def Write(self):
       print('<b>Анамнез</b> <br>')
       print('ФИО: {}<br> Возраст: {}<br> Амплуа: {}<br> Команда: {}<br>'.format(self.name, self.age, self.line, self.team))

    def ShowEdit(self):
        super().ShowEdit()
        print('<tr><td>Команда:</td><td><input type="text" name="team" value="{0}"></td></tr>'.format(self.team))
        
    def SaveEdit(self, q):
        super().SaveEdit(q)
        self.team = q.getvalue('team')
