import cgi

class Phone:
    
    def __init__(self, q, selfurl):
        self.q=q
        self.selfurl=selfurl
        self.mark=""
        self.model=""
        self.num=""
        self.price=""
       
    def read(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("name","--")
        if ('mark' in self.q):
            self.mark = self.q['mark'].value
        else: self.mark=""
        if ('model' in self.q):
            self.model = self.q['model'].value
        else: self.model = ""
        if ('num' in self.q):
            self.num = self.q['num'].value
        else: self.num = ""
        if ('price' in self.q):
            self.price = self.q['price'].value
        else: self.price = ""
        
    def show_form(self):
        self.q = cgi.FieldStorage()
        self.q.getfirst("id","--")
        print('<form action="{0}?student={1}&selection=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="selection" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('<table>')
        print('<td align="right" width="100">Марка</td><td><input type="text" name="mark" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.mark))
        print('<td align="right" width="100">Модель</td><td><input type="text" name="model" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.model))
        print('<td align="right" width="100">Количество</td><td><input type="text" name="num" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.num))
        print('<td align="right" width="100">Стоимость</td><td><input type="text" name="price" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.price))
                
    def show_values(self):
        print('<td>{0}</td>'.format(self.mark))
        print('<td>{0}</td>'.format(self.model))
        print('<td>{0}</td>'.format(self.num))
        print('<td>{0}</td>'.format(self.price))
