from .clStudent import *
from .clRgungStud import *
import pickle

class ASM:   
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl
        self._student = []
       
    def show(self,q, selfurl):
        tmp_list = []
        count = 1
        for e in self._student:
            tmp_list.append(LoadTpl('actions').format(str(e),selfurl, q['student'].value,str(count))) 
            count +=  1
        return print(LoadTpl('table').format("".join(tmp_list)))
     
    def readf(self):
        self._student = pickle.load( open( "cgi-bin/st33/toload.txt", "rb" ) )
        
    def writef(self):
        pickle.dump(self._student, open( "cgi-bin/st33/toload.txt", "wb" ) )     

    def edit(self, q, selfurl):
        studnum = q.getfirst("num", None)
        if studnum!=None and int(studnum)<=len(self._student):#to edit
            stype=type(self._student[int(studnum)-1])
            name1=self._student[int(studnum)-1]._name
            age1=self._student[int(studnum)-1]._age
            try:
                lastgroup1=self._student[int(studnum)-1]._lastgroup
            except:
                bachelor1=self._student[int(studnum)-1]._bachelor
                
        else:#to add
             studnum=len(self._student)+1
             name1=""
             age1=""
             bachelor1=""
             lastgroup1=""
             typeadd = q.getfirst("typeadd", None)
             if typeadd=="1":
                 stype=type(RgungStud(None,0,None,None))
             elif typeadd=="2":
                 stype=type(Student(None,0,None))
                 
        name=q.getfirst("name", None)
        age=q.getfirst("age", 0)
        if stype is RgungStud:
            lastgroup=q.getfirst("lastgroup", None)
            if name==None or age==0 or lastgroup==None:           
                print (LoadTpl('editrgung').format(selfurl,q['student'].value,studnum,name1,age1,lastgroup1))
                fl=1
            else:
                fl=0
            student = RgungStud(None,0,"РГУНГ",None).getForm(q)   
        else:
            bachelor=q.getfirst("bachelor", None)
            if name==None or age==0 or bachelor==None:           
                print (LoadTpl('editstud').format(selfurl,q['student'].value,studnum,name1,age1,bachelor1))
                fl=1
            else:
                fl=0
            student = Student(None,0,None).getForm(q)    
        
        if fl==0:
            studnum = q.getfirst("num", None)
            if studnum!=None and int(studnum)<=len(self._student):
                self._student[int(studnum)-1] = student
            else:
                self.readf()
                self._student.append(student)   
            self.writef()        
        return
    
    def delete(self, q, selfurl):
        studnum = q.getfirst("num", None)
        self._student.pop(int(studnum)-1)
        self.writef()
        return


 
