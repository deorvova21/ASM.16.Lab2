from .Car import *
class Driver(Car):
    def __init__(self):
        super().__init__()
        self.dname=''
        self.lastname=''
        self.age=''
        

    def write(self):
       print('<b>Driver:</b> <br>')
       print('cName: {0}<br> Color: {1}<br> Price: {2}<br> dName: {3}<br> Lastname: {4}<br> Age: {5}<br>'.format(self.cname, self.color, self.price, self.dname, self.lastname, self.age))

    def show_car(self):
        super().show_car()
        print('<tr><td>Name:</td><td><input type="text" name="dname" value="{0}"></td></tr>'.format(self.dname))
        print('<tr><td>Lastname:</td><td><input type="text" name="lastname" value="{0}"></td></tr>'.format(self.lastname))
        print('<tr><td>Age:</td><td><input type="text" name="age" value="{0}"></td></tr>'.format(self.age))


        
    def edit_car(self, q):
        super().edit_car(q)
        self.dname = q.getvalue('dname')
        self.lastname = q.getvalue('lastname')
        self.age = q.getvalue('age')
