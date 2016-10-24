import cgi
class Car:
    def __init__(self):
        self.cname=''
        self.color=''
        self.price='' 

    def write(self):
        print('<b>Car:</b> <br>')
        print('cName: {0}<br> Color: {1}<br> Price: {2}<br><br>'.format(self.cname, self.color, self.price))

    def show_car(self):
        print('<tr><td>Name:</td><td><input type="text" name="cname" value="{0}"></td><tr>'.format(self.cname))
        print('<tr><td>Color:</td><td><input type="text" name="color" value="{0}"></td></tr>'.format(self.color))
        print('<tr><td>Price:</td><td><input type="text" name="price" value="{0}"></td></tr>'.format(self.price))
        
        
    def edit_car(self, q):
        self.cname = q.getvalue('cname')
        self.color = q.getvalue('color')
        self.price = q.getvalue('price')
        

            
