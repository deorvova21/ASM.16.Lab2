import pickle, cgi, os
from .anamnesis import *

class List:
    def __init__(self, q, selfurl):
        self.patients = []
        self.q = q
        self.selfurl = selfurl

    def AddPatient(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addpatient" />')
        print('<table>')
        Patient().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def AddAnamnesis(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addanamnesis" />')
        print('<table>')
        Anamnesis().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def ShowList(self):
        i = 0
        for item in self.patients:
            print('<br>')
            item.Write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<br>')
            i+=1
        print('<br>')
        print('<a href={0}?student={1}&act=addpatient>Добавить пациента</a> '.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=addanamnesis>Добавить анамнез</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}>Назад</a>'.format(self.selfurl))

    def Get(self):
        if self.q.getvalue('id') == 'addpatient':
            pat = Patient()
            pat.SaveEdit(self.q)
            self.patients.append(pat)
        elif self.q.getvalue('id') == 'addanamnesis':
            pat = Anamnesis()
            pat.SaveEdit(self.q)
            self.patients.append(pat)
        else:
            self.patients[int(self.q.getvalue('id'))].SaveEdit(self.q)
        self.ShowList()

    def Edit(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        iid = self.q.getvalue('id')
        print('<input type="hidden" name="id" value="{0}" />'.format(iid))
        print('<table>')
        self.patients[int(iid)].ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def Save(self):
        pickle.dump(self.patients, open('cgi-bin/st33/patients.bin', 'wb'))

    def Load(self):
        if (os.path.exists('cgi-bin/st33/patients.bin')):
            self.patients = pickle.load(open('cgi-bin/st33/patients.bin', 'rb'))

    def Delete(self):
        self.patients.pop(int(self.q.getvalue('id')))
        self.ShowList()

    def Clear(self):
        self.patients.clear()
        self.ShowList()
