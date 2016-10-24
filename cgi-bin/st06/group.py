import pickle, os
from .student import *
from .mayor import *

class Group:
    def __init__(self):
        self.l=list()
        
    def read(self):
        print("Введите цифру соотвествующего класса\n1 - Студент\n2 - Староста")
        print("Для возврата в предыдуще меню нажмите 0")
        k = input()
        if (k=="0"): return
        if (k=="1"): self.l.append(Student())
        elif (k=="2"): self.l.append(Mayor())
        else:
            print("Введено некорректное значение")
            self.read()
        
    def write(self):
        i=1
        for o in self.l:
            print("Элемент", i)
            o.write()
            i+=1
            print("")
        if (len(self.l)==0):
            print("Список пуст")
    
    def cd(self,i):
        self.write()
        if (len(self.l)==0): return
        print("Для изменения выберите номер элемента в списке")
        print("Для возврата в предыдуще меню нажмите 0")
        try:
            m = int(input())
            if (m==0): return
            if (i==1):    
                self.l[m-1].read()
                print("Изменено!")
            if (i==2):
                self.l.pop(m-1)
                print("Удалено!")
        except:
            print("Введено некорректное значение")
            self.cd(i)                
            
    def change(self):
        self.cd(1)

    def delete(self):
        self.cd(2)
                  
    def read_file(self):
        if (os.path.exists("st06/list.dat")):
            self.l = pickle.load(open("st06/list.dat", "rb"))
            print("Список считан!")
        else:
            print("Ошибка чтения файла!")
     
    def write_file(self):
            pickle.dump(self.l, open("st06/list.dat", "wb"))
            print("Список записан в файл!")

    def clear(self):
        self.l.clear()
        print("Список очищен!")
        
    

    
