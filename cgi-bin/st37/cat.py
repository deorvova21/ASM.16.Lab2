from .feline import *

class Cat(Feline):
    __kind='Cat'
    __name='None'
    __owner='None'
    def __init__(self,name = 'unnamed',owner='None', kind='Cat', age=0,weight=0):
        Feline.__init__(self,kind, age, weight)
        self.setName(name)
        self.setOwner(owner)

    def setName(self, value):
        self.__name=value
    def setOwner(self, value):
        self.__owner=value

    def getName(self):
        return self.__name
    
    def getOwner(self):
        return self.__owner
    
    def getFromForm(self, q):
        Feline.getFromForm(self, q)
        self.setName(q.getfirst('Name', None))
        self.setOwner(q.getfirst('Owner', None))
    
    def getInputs(self, q):
        kind = q.getfirst('Kind', self.getKind())
        age = q.getfirst('Age', self.getAge())
        weight = q.getfirst('Weight', self.getWeight())
        name = q.getfirst('Name', self.getName())
        owner = q.getfirst('Owner', self.getOwner())
        return """ <input placeholder="input kind" value = """ + '"' + kind + '"' + """ type="text" name="Kind">
        <input placeholder="input age" value = """ + '"' + age + '"' + """ type="text" name="Age">
        <input placeholder="input weight" value = """ + '"' + weight + '"' + """ type="text" name="Weight">""" + """ <input placeholder="input name" value = """ + '"' + name + '"' + """ type="text" name="Name">
        <input placeholder="input owner's name" value = """ + '"' + owner + '"' + """ type="text" name="Owner">"""
        
    def print_object(self):
        return '<td>' + str(self.getKind()) + '</td><td>' + str(self.getAge()) + '</td><td>' + str(self.getWeight()) + '</td><td>' + str(self.getName()) + '</td><td>' + str(self.getOwner()) + '</td>'       
    
