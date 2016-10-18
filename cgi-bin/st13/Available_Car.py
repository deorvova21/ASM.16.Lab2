import cgi,datetime

class Available_Car:
    def __init__(self):
        self.model=''
        self.color=''
        self.HP=''
        self.price=''
        self.time = datetime.datetime.now()


    def write(self):
        print('<b>Автомобиль в наличии:</b> <br>')
        print('Модель: {0}<br> Цвет: {1}<br> Мощность л.с. {2}<br> Цена: {3}<br> Дата записи: {4}<br>'.format(self.model, self.color, self.HP, self.price, self.time))

    def show_car(self):
        print('<tr><td>Модель:</td><td><input type="text" name="model" value="{0}"></td><tr>'.format(self.model))
        print('<tr><td>Цвет:</td><td><input type="text" name="color" value="{0}"></td></tr>'.format(self.color))
        print('<tr><td>Мощность:</td><td><input type="text" name="HP" value="{0}"></td></tr>'.format(self.HP))
        print('<tr><td>Цена:</td><td><input type="text" name="price" value="{0}"></td></tr>'.format(self.price))
        print('<tr><td>Время записи:</td><td><input type="text" name="time" value="{0}"></td></tr>'.format(self.time))
        
    def edit_car(self, q):
        self.model = q.getvalue('model')
        self.color = q.getvalue('color')
        self.HP = q.getvalue('HP')
        self.price = q.getvalue('price')
        self.time = datetime.datetime.now()
