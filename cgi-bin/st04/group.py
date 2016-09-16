from .monitor import *
import pickle
class Group:
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self._student = []
    def add(self, x):
        self._student.append(x)
    def edit(self, num, name, age, grants, address, phone, email):
        self._student[num].setName(name)
        self._student[num].setAge(age)
        self._student[num].setGrants(grants)
        self._student[num].setAddress(address)
        if type(self._student[num]) is Monitor:
            self._student[num].setPhone(phone)
            self._student[num].setEmail(email)
    def delete(self,num):
        self._student.pop(num)
    def clear(self):
        self._student = []
    def check(self,num):
        return self._student[num].getName()
    def load(self):
        self._student = pickle.load( open( "cgi-bin/st04/04.p", "rb" ) )
    def save(self):
        pickle.dump( self._student, open( "cgi-bin/st04/04.p", "wb" ) )
    def checkClass(self,num):
        if type(self._student[num]) is Monitor:
            return "Monitor"
        else:
            return "Student"
    def getName(self,num):
        return self._student[num].getName()
    def getAge(self,num):
        return self._student[num].getAge()
    def getGrants(self,num):
        return self._student[num].getGrants()
    def getAddress(self,num):
        return self._student[num].getAddress()
    def getPhone(self,num):
        return self._student[num].getPhone()
    def getEmail(self,num):
        return self._student[num].getEmail()
    def __len__(self):
        return len(self._student)
    def __str__(self):
        tmp_list = []
        count = 1
        if self._student:
            for e in self._student:
                tmp_list.append( "<tr>" + str(e) + """<th> <a href="{0}?student={1}&choice=2&num=""".format(self.selfurl, self.q['student'].value) + str(count) +"""">Редактировать</a> | 
                    <a href="{0}?student={1}&choice=3&num=""".format(self.selfurl, self.q['student'].value) + str(count) +"""">Удалить</a></th></tr>""")
                count +=  1
            tmp_string = "<br>".join(tmp_list)
            tmp_string = """<table border="1">
   <caption>Картотека</caption>
   <tr>
    <th>Тип</th>
    <th>Имя</th>
    <th>Возраст</th>
    <th>Стипендия</th>
    <th>Адрес</th>
    <th>Телефон</th>
    <th>Эл. почта</th>
    <th>Действие</th>
   </tr>""" + tmp_string + "</table>"
            
        else:
            tmp_string="Empty list\n"
        return tmp_string