class class1:
    def __init__ (self):
        self.num1 = ''
        self.num2 = ''
        self.num3 = ''
    def write (self):
        print('<td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td>'.format(self.num1, self.num2, self.num3, '---', '---'))
    def show (self):
        print('<tr><td>Поле1:</td><td><input type="text" name="num1"value="{0}"></td></tr>'.format(self.num1))
        print('<tr><td>Поле2:</td><td><input type="text" name="num2"value="{0}"></td></tr>'.format(self.num2))
        print('<tr><td>Поле3:</td><td><input type="text" name="num3"value="{0}"></td></tr>'.format(self.num3))
    def edit (self, q):
        self.num1 = q.getvalue('num1')
        self.num2 = q.getvalue('num2')
        self.num3 = q.getvalue('num3')

