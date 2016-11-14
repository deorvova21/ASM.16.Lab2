import os,re,sys,cgi,pickle
from .student import *
from .starosta import *
from .loadtpl import *
import pickle
class group:
        def __init__(self,q,selfurl):
                self.spisok = []
                self.q=q
                self.selfurl=selfurl
        def delete(self):
                self.readf()
                self.spisok.pop(int(self.q['iid'].value))
                self.writef()
                self.showstudents()
        def editform(self):
                self.readf()
                self.spisok[int(self.q['iid'].value)].editform(self.q)
        def edit(self):
                self.readf()
                self.spisok[int(self.q['iid'].value)].edit(self.q) 
                self.writef()
                self.showstudents()
        def showstudents(self):
                self.readf()
                print(loadtpl('table'))
                j=0
                if len(self.spisok)>0:
                        for i in self.spisok:
                                i.iid=j
                                j=j+1
                                i.show()
                print(loadtpl('buttons').format(self.q['student'].value, self.selfurl))
        def clear(self):
                self.spisok.clear()
                self.writef()
                self.showstudents()

        def studentform(self):
                student_tmp=student(self.q)
                student_tmp.addform()
        def starostaform(self):
                starosta_tmp=starosta(self.q)
                starosta_tmp.addform()
        def addstudent(self):
                self.readf()
                student_tmp=student(self.q)
                student_tmp.edit(self.q)
                self.spisok.append(student_tmp)
                self.writef()
                self.showstudents()
        def addstarosta(self):
                self.readf()
                starosta_tmp=starosta(self.q)
                starosta_tmp.edit(self.q)
                self.spisok.append(starosta_tmp)
                self.writef()
                self.showstudents()
                
        def writef(self):
                pickle.dump(self.spisok, open('cgi-bin/st09/file.txt', 'wb'))
        def readf(self):
                if (os.path.exists('cgi-bin/st09/file.txt')):
                        self.spisok=pickle.load(open('cgi-bin/st09/file.txt', 'rb'))
