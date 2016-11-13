import os,re,sys,cgi,pickle
from .student import *
from .starosta import * 
class Group:
        
        def __init__(self,q,selfurl):
                self.q=q
                self.students=[]
                self.selfurl=selfurl
               
        def AddStudentForm(self):
                self.ReadFile()
                student=Student(self.q)                
                student.AddPersonForm()
                
        def AddStudent(self):
                self.ReadFile()
                student=Student(self.q)
                student.EditPerson(self.q)
                self.students.append(student)
                self.WriteFile()
                self.Display()
                
        def AddStarosta(self):
                self.ReadFile()
                starosta=Starosta(self.q)
                starosta.EditPerson(self.q)
                self.students.append(starosta)               
                self.WriteFile()
                self.Display()
                
        def AddStarostaForm(self):
                self.ReadFile()
                starosta=Starosta(self.q)
                starosta.AddPersonForm()
                
        def EditForm(self):
                self.ReadFile()
                self.students[int(self.q['iid'].value)].EditForm(self.q)
                

        def Edit(self):
               self.ReadFile()
               self.students[int(self.q['iid'].value)].EditPerson(self.q) 
               self.WriteFile()
               self.Display()

               
        def Delete(self):
                self.ReadFile()
                self.students.pop(int(self.q['iid'].value))
                self.WriteFile()
                self.Display()
        def Display(self):
                self.ReadFile()
                print('<table  border="1"><tr><td>Имя</td><td>Возраст</td><td>Город</td><td>Средний бал</td><td>Телефон</td><td>Действия</td></tr>')
                iid=0
                if(len(self.students)>0):
                        for i in self.students:
                                i.WritePerson(iid)
                                iid+=1
                print('</table>')
                print("""
<a href="?student={0}&type=AddStarForm">Добавить старосту</a> | <a href="?student={0}&type=AddStudForm">Добавить студента</a>
| <a href="?student={0}&type=Clear">Удалить всех</a><br> <a href="{1}">Назад</a>
""".format(self.q['student'].value, self.selfurl))
        def Clear(self):
                        self.ReadFile()
                        self.students.clear()
                        self.WriteFile()
                        self.Display()
        def WriteFile(self):
                with open('cgi-bin/st29/file.txt', 'wb') as file:
                    pickle.dump(self.students, file)
        def ReadFile(self):
                if (os.path.exists('cgi-bin/st29/file.txt')):
                    with open('cgi-bin/st29/file.txt', 'rb') as file:
                        self.students = pickle.load(file)
            



