import cgi
class Game_AAA:
    def __init__(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        self.name=""
        self.developer=""
        self.Publisher=""
        self.ReleaseDate=""
        self.Genre=""
        self.Price=""

        
    def read(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("name","--")
        if ('name' in self.q):
            self.name = self.q['name'].value
        else: self.name=""
        if ('developer' in self.q):
            self.developer = self.q['developer'].value
        else: self.developer = ""
        if ('Publisher' in self.q):
            self.Publisher = self.q['Publisher'].value
        else: self.Publisher = ""
        if ('ReleaseDate' in self.q):
            self.ReleaseDate = self.q['ReleaseDate'].value
        else: self.ReleaseDate = ""
        if ('Genre' in self.q):
            self.Genre = self.q['Genre'].value
        else: self.Genre = ""
        if ('Price' in self.q):
            self.Price = self.q['Price'].value
        else: self.Price = ""
        
    def write_ch(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('Name:<br><input type="text" name="name" value="{0}">'.format(self.name))
        print('<br>developer:<br><input type="text" name="developer" value="{0}">'.format(self.developer))
        print('<br>Publisher:<br><input type="text" name="Publisher" value="{0}">'.format(self.Publisher))
        print('<br>ReleaseDate:<br><input type="text" name="ReleaseDate" value="{0}">'.format(self.ReleaseDate))
        print('<br>Genre:<br><input type="text" name="Genre" value="{0}">'.format(self.Genre))
        print('<br>Price:<br><input type="text" name="Price" value="{0}">'.format(self.Price))

    def write(self):
        print('<td>{0}</td>'.format(self.name))
        print('<td>{0}</td>'.format(self.developer))
        print('<td>{0}</td>'.format(self.Publisher))
        print('<td>{0}</td>'.format(self.ReleaseDate))
        print('<td>{0}</td>'.format(self.Genre))
        print('<td>{0}</td>'.format(self.Price))
