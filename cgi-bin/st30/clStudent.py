from .loadtpl import *
class Student:
    def __init__(self,name, age, bachelor):
        self._name = name 
        self._age = age
        self._bachelor = bachelor
        
    def getForm(self, q):
        self._name = q.getfirst("name", None)
        self._age = q.getfirst("age", 0)
        self._bachelor = q.getfirst("bachelor", None)
        return self
        
    def __str__(self):
        return LoadTpl('strstud').format(str(self._name),str(self._age),str(self._bachelor))

    