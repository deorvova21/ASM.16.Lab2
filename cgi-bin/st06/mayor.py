from .student import *

class Mayor(Student):
    def __init__(self):
        super().__init__()
        self.telephone = ""
    
    def read(self):
        Student.read(self)
        print("Введите номер телефона:")
        self.telephone = input()

    def write(self):
        Student.write(self)
        print("Номер телефона:", self.telephone)
    
    
