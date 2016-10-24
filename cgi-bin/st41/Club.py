import os,re,sys,cgi,pickle
from .Descendant import *
from .LoadTpl import *

class Club:
    def __init__(self, q, selfurl):
        self.q=q
        self.list=[]
        self.selfurl=selfurl
        
    def AddSkater(self):
        self.FileReading()
        skater=Skater(self.q)
        self.list.append(skater)
        skater.showform()
        skater.edit(self.q)
        self.FileRecording()
           
    def AddDescendant(self):
        self.FileReading()
        descendant=Descendant(self.q)
        self.list.append(descendant)
        descendant.showform()
        descendant.edit(self.q)
        self.FileRecording()              
        
    def Edit(self):
        self.FileReading()
        self.list[int(self.q['i'].value)].edit(self.q)
        self.FileRecording()
        self.PrintList()
        
    def FileReading(self): 
        if (os.path.exists('cgi-bin/st41/file.db')):
            with open('cgi-bin/st41/file.db', 'rb') as f:
                self.list = pickle.load(f)

    def FileRecording(self): 
        with open('cgi-bin/st41/file.db', 'wb') as f:
            pickle.dump(self.list, f)            
            
    def Change(self):    
        self.FileReading()
        item=self.list[int(self.q['i'].value)]
        item.change(self.q)       
     
    def DeleteElement(self):
        self.FileReading()
        self.list.pop(int(self.q['i'].value))
        self.FileRecording()
        self.PrintList()
        
    def DeleteList(self):
        self.FileReading()
        self.list.clear()
        self.FileRecording()
        self.PrintList()                
    
    def PrintList(self):
        self.FileReading()
        i=0
        for item in self.list:
            item.show(self.q, i)
            i+=1
        print(LoadTpl('club').format(self.q['student'].value, self.selfurl))         
        
        
    
