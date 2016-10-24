import cgi

class Emploee:
        def __init__(self, q):
                self.q = q
                self.name = " "
                self.dep = " "
                self.phone = " "

        def add(self): 
                print('<Caption><H3>Add Emploee</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="add_emploee">')
                print('<table border="0"><tr><td>Name:</td><td><input type=text name=name value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.name))
                print('<tr><td>Department</td><td><input type=text name=dep value="{0}"></td></tr>'.format(self.dep))
                print('<tr><td>Phone</td><td><input type=text name=phone value="{0}"></td></tr>'.format(self.phone))
                print('<br><input type=submit value="Ok"> </form>')
                print('<a href="?student={0}">Back</a>'.format(self.q['student'].value))
                
        def save_form(self, q):
                if 'name' in self.q:
                        self.name = q.getvalue('name')
                else: self.name=" "
                self.dep = q.getvalue('dep')
                self.phone = q.getvalue('phone')

        def show_form(self):
                print('<tr>')
                print('<td>{0}</td>'.format(self.name))
                print('<td>{0}</td>'.format(self.dep))
                print('<td>{0}</td>'.format(self.phone))
                print('<th colspan="2">None</th>')

        def edit_obj(self, q):
                print('<Caption><H3>Edit object</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="edit">')
                print('<input type=hidden name=id value={0}>'.format(q['id'].value))
                print('<table border="0"><tr><td>Name</td><td><input type=text name=name value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.name))
                print('<tr><td>Depertment</td><td><input type=text name=dep value="{0}"></td></tr>'.format(self.dep))
                print('<tr><td>Phone</td><td><input type=text name=phone value="{0}"></td></tr>'.format(self.phone))
                print('<br><input type=submit value="Ok"> </form>')
                print('<a href="?student={0}">Back</a>'.format(self.q['student'].value))
               

