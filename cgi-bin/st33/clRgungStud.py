from .clStudent import *

class RgungStud(Student):
    def __init__(self,name, age, bachelor,lastgroup):
        Student.__init__(self,name, age, bachelor)
        self._lastgroup = lastgroup

    def getForm(self, q):        
        Student.getForm(self, q)
        self._lastgroup = q.getfirst("lastgroup", None)
        return self
        
    def __str__(self):
        return LoadTpl('strrgung').format(str(self._name),str(self._age),str(self._lastgroup))
        
        
