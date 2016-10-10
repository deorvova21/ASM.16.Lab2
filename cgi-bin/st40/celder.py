from .cstudent import *

class Elder(Student):
    def __init__(self):
        super().__init__()
        self.allowance=''
    
    def print_me(self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>'.format(self.name, self.dob, self.group, self.allowance))

    def show_edit(self):
        super().show_edit()
        print('<tr><td>Надбавка:</td><td><input type="text" name="allowance" value="{0}"></td></tr>'.format(self.allowance))

    def edit_me(self, q):
        super().edit_me(q)
        self.allowance = q.getvalue('allowance')
