class Budget:
    def __init__(self):
        self.iid = 0
        self.fio= ''
        self.ball= ''
        self.group= ''

    def write_type(self):
        print('<b>Бюджетный студент:</b>')

    def write(self):
        self.write_type()
        print('<br> ФИО: {0}<br> Ср. балл: {1}<br> Группа: {2}<br>'.format(self.fio, self.ball, self.group))

    def show_stud(self):
        print('<tr><td>ФИО:</td><td><input type="text" name="fio" value="{0}"></td><tr>'.format(self.fio))
        print('<tr><td>Ср. балл:</td><td><input type="text" name="ball" value="{0}"></td></tr>'.format(self.ball))
        print('<tr><td>Группа:</td><td><input type="text" name="group" value="{0}"></td></tr>'.format(self.group))

    def edit_stud(self, q):
        self.fio = q.getvalue('fio')
        self.ball = q.getvalue('ball')
        self.group = q.getvalue('group')

