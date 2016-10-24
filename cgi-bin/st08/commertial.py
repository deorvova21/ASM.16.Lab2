from .budget import *

class Commertial(Budget):
    def __init__(self):
        super().__init__()
        self.oplata = ''

    def write_type(self):
        print('<b>Коммерческий студент:</b>')
        
    def write(self):
        super().write()
        print('Оплата за обучение: {0}<br>'.format(self.oplata))

    def show_stud(self):
        super().show_stud()
        print('<tr><td>Оплата за обучение:</td><td><input type="text" name="oplata" value="{0}"></td></tr>'.format(self.oplata))

    def edit_stud(self, q):
        super().edit_stud(q)
        self.oplata = q.getvalue('oplata')
