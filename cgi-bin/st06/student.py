class Student:
    def __init__(self):
        self.name = ""
        self.sex = ""
        self.age = ""
        self.grants = ""      
        
    def read(self):
        print("Введите имя:")
        self.name = input()
        print("Введите пол:")
        self.sex = input()
        print("Введите возраст:")
        self.age = input()
        print("Введите размер стипендии:")
        self.grants = input()
        
    def write(self):
        print("Имя:", self.name)
        print("Пол:", self.sex)
        print("Возраст:", self.age)
        print("Размер стипендии:", self.grants)
