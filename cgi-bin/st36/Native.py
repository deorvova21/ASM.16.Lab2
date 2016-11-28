import cgi

class Native:
    def __init__(self):
        self.bandname = ''
        self.albumname = ''
        self.year = ''
        self.songs = ''
        
    def Write(self):
        print('<b>Альбом российской группы</b> <br>')
        print('Группа: {}<br> Альбом: {}<br> Год: {}<br> Кол-во песен: {}<br>'.format(self.bandname, self.albumname, self.year, self.songs))

    def ShowEdit(self):
        print('<tr><td>Группа:</td><td><input type="text" name="bandname" value="{0}"></td><tr>'.format(self.bandname))
        print('<tr><td>Альбом:</td><td><input type="text" name="albumname" value="{0}"></td></tr>'.format(self.albumname))
        print('<tr><td>Год:</td><td><input type="text" name="year" value="{0}"></td></tr>'.format(self.year))
        print('<tr><td>Кол-во песен:</td><td><input type="text" name="songs" value="{0}"></td></tr>'.format(self.songs))
        
    def SaveEdit(self, q):
        self.bandname = q.getvalue('bandname')
        self.albumname = q.getvalue('albumname')
        self.year = q.getvalue('year')
        self.songs = q.getvalue('songs')
