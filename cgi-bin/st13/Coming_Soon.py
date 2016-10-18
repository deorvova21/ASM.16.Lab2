from .Available_Car import *

class Coming_Soon(Available_Car):
    def __init__(self):
        super().__init__()
        self.date=''
        self.country=''
    
    def write(self):
       print('<b>Автомобиль ожидается:</b> <br>')
       print('Модель: {0}<br> Цвет: {1}<br> Мощность л.с. {2}<br> Цена: {3}<br> Дата записи: {4}<br> Дата поставки: {5}<br> Страна поставщик: {6}<br>'.format(self.model, self.color, self.HP, self.price, self.time, self.date, self.country))

    def show_car(self):
        super().show_car()
        print('<tr><td>Дата поставки:</td><td><input type="text" name="date" value="{0}"></td></tr>'.format(self.date))
        print('<tr><td>Страна поставки:</td><td><input type="text" name="country" value="{0}"></td></tr>'.format(self.country))
        
    def edit_car(self, q):
        super().edit_car(q)
        self.date = q.getvalue('date')
        self.country = q.getvalue('country')
