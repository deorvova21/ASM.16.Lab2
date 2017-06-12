import os,re,sys,cgi,pickle
from .ProfessionalFootballPlayer import *
from .FootballPlayer import *
from .LoadTpl import *

class container:
    def __init__(self,q,selfurl):
        self.q=q
        self.list=[]
        self.selfurl=selfurl
        
    def AddFP(self):
        self.Read()
        FP=FootballPlayer(self.q)
        self.list.append(FP)
        FP.ShowForm()
        FP.Edit(self.q)
        self.Write()
        
              
    def AddPFP(self):
        self.Read()
        PFP=ProfessionalFootballPlayer(self.q)
        self.list.append(PFP)
        PFP.ShowForm()
        PFP.Edit(self.q)
        self.Write()
        
        
    def Edit(self):
        self.Read()
        self.list[int(self.q['i'].value)].Edit(self.q)
        self.Write()
        self.ShowGroup()
        
    def Read(self):
        #if (os.path.exists('cgi-bin/st43/file.dat')):
        with open("cgi-bin/st43/file.dat","rb") as file:
            self.list = pickle.load(file)     
            
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
        with open('cgi-bin/st43/file.dat', 'wb') as f:
            pickle.dump(self.list, f)
            
    def ShowGroup(self):
        self.Read()
        i=0
        for item in self.list:
            item.Show(self.q, i)
            i+=1
        print(LoadTpl('container').format(self.q['student'].value, self.selfurl))
    

