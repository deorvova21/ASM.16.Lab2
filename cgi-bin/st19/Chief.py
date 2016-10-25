from .Emploee import Emploee
import cgi

class Chief(Emploee):
        def __init__(self, q):
                super().__init__(q)
                self.lname = " "
                self.stat = " "
                
        def add(self): 
                print('<Caption><H3>Add Chief</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="add_chief">')
                print('<table border="0"><tr><td>Name:</td><td><input type=text name=name value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.name))
                print('<tr><td>Department</td><td><input type=text name=dep value="{0}"></td></tr>'.format(self.dep))
                print('<tr><td>Phone</td><td><input type=text name=phone value="{0}"></td></tr>'.format(self.phone))
                print('<tr><td>Last Name</td><td><input type=text name=lname value="{0}"></td></tr>'.format(self.lname))
                print('<tr><td>Status</td><td><input type=text name=stat value="{0}"></td></tr>'.format(self.stat))
                print('<br><input type=submit value="Ok"> </form>')
                print('<a href="?student={0}">Back</a>'.format(self.q['student'].value))
                
        def save_form(self, q):
                super().save_form(q)
                self.lname = q.getvalue('lname')
                self.stat = q.getvalue('stat')

        def show_form(self):
                print('<tr>')
                print('<td>{0}</td>'.format(self.name))
                print('<td>{0}</td>'.format(self.dep))
                print('<td>{0}</td>'.format(self.phone))
                print('<td>{0}</td>'.format(self.lname))
                print('<td>{0}</td>'.format(self.stat))

        def edit_obj(self, q):
                super().edit_obj(q)
                print('<tr><td>Last Name</td><td><input type=text name=lname value="{0}"></td></tr>'.format(self.lname))
                print('<tr><td>Status</td><td><input type=text name=stat value="{0}"></td></tr>'.format(self.stat))
               

