from .Native import *

class Foreign(Native):
    def __init__(self):
        super().__init__()
        self.country = ''
        
    def Write(self):
       print('<b>Альбом зарубежной группы</b> <br>')
       print('Группа: {}<br> Альбом: {}<br> Год: {}<br> Кол-во песен: {}<br> Страна: {}<br>'.format(self.bandname, self.albumname, self.year, self.songs, self.country))

    def ShowEdit(self):
        super().ShowEdit()
        print('<tr><td>Страна:</td><td><input type="text" name="country" value="{0}"></td></tr>'.format(self.country))
        
    def SaveEdit(self, q):
        super().SaveEdit(q)
        self.country = q.getvalue('country')
