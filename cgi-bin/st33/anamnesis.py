from .patient import *

class Anamnesis(Patient):
    def __init__(self):
        super().__init__()
        self.diagnosis = ''
        
    def Write(self):
       print('<b>Анамнез</b> <br>')
       print('ФИО: {}<br> Возраст: {}<br> Симптоматика: {}<br> Диагноз: {}<br>'.format(self.name, self.age, self.symptoms, self.diagnosis))

    def ShowEdit(self):
        super().ShowEdit()
        print('<tr><td>Диагноз:</td><td><input type="text" name="diagnosis" value="{0}"></td></tr>'.format(self.diagnosis))
        
    def SaveEdit(self, q):
        super().SaveEdit(q)
        self.diagnosis = q.getvalue('diagnosis')
