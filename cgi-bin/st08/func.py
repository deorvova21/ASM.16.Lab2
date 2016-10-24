import pickle, cgi, os, sys, re
from .budget import *
from .commertial import *

class functions:
    def __init__(self,q,selfurl):
        self.stud= []
        self.q = q
        self.selfurl = selfurl

    def load(self):
        if (os.path.exists('cgi-bin/st08/file.dat')):
            self.stud = pickle.load(open('cgi-bin/st08/file.dat', 'rb'))

    def doadd_bud(self):
        bud = Budget()
        self.stud.append(bud)
        self.edit(bud, st1)
        
    def doadd_comm(self):
        comm = Commertial()
        self.stud.append(comm)
        self.edit(comm, st2)
        return 0
    
    def dodel(self):
        self.stud.pop(int(self.q.getvalue('id')))
        self.showform()
        return 0
      
    def save(self):
        pickle.dump(self.stud, open('cgi-bin/st08/file.dat', 'wb'))
    
    def showform(self):
        i = 0
        for item in self.stud:
            item.write()
            print("""
<a href={0}?student={1}&act=edit&id={2}>Редактировать </a>
<a href={0}?student={1}&act=delete&id={2}> Удалить</a><br><br>""".format(self.selfurl, self.q['student'].value, i))
            i+=1

        print("""
<input type="hidden" name="student" value={0} />
<p><a href={1}?student={0}&act=doadd_bud>Добавить бюджетника</a>
<p><a href={1}?student={0}&act=doadd_comm>Добавить платника</a>
<p><a href={1}>Назад</a>
</form>""".format(self.q['student'].value,self.selfurl))
        
    def edit(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="gett" />')
        act = self.q.getvalue('act')
        if act == 'edit':
            studid = self.q.getvalue('id')
        else:
            studid = str(len(self.stud)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(studid))
        print('<table>')
        self.stud[int(studid)].show_stud()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def gett(self):
        self.stud[int(self.q.getvalue('id'))].edit_stud(self.q)
        self.showform()
