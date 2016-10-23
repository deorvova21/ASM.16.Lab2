import os,re,sys,cgi,pickle
from .Graduate import *
from .LoadTpl import *

class Group:
    def __init__(self,q,selfurl):
        self.q=q
        self.list=[]
        self.selfurl=selfurl
        
    def AddStud(self):
        self.Read()
        stud=Student(self.q)
        self.list.append(stud)
        stud.ShowForm()
        stud.Edit(self.q)
        self.Write()
        
              
    def AddGrad(self):
        self.Read()
        grad=Graduate(self.q)
        self.list.append(grad)
        grad.ShowForm()
        grad.Edit(self.q)
        self.Write()
        
        
    def Edit(self):
        self.Read()
        self.list[int(self.q['i'].value)].Edit(self.q)
        self.Write()
        self.ShowGroup()
        
    def Read(self):
        if (os.path.exists('cgi-bin/st07/file.db')):
            with open('cgi-bin/st07/file.db', 'rb') as f:
                self.list = pickle.load(f)
            
    def Change(self):
        self.Read()
        item=self.list[int(self.q['i'].value)]
        item.Change(self.q)       
        
        
        
    def Delete(self):
        self.Read()
        self.list.pop(int(self.q['i'].value))
        self.Write()
        self.ShowGroup()
        
    def Clear(self):
        self.Read()
        self.list.clear()
        self.Write()
        self.ShowGroup()
                
    def Write(self):
        with open('cgi-bin/st07/file.db', 'wb') as f:
            pickle.dump(self.list, f)
            
    def ShowGroup(self):
        self.Read()
        i=0
        for item in self.list:
            item.Show(self.q,i)
            i+=1
        print(LoadTpl('group').format(self.q['student'].value, self.selfurl))
    
