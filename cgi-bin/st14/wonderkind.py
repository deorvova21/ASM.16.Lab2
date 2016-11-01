from .children import Children
import cgi

class Wonderkind(Children):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.power=""
        self.q=q
        self.selfurl=selfurl
    
    def read(self):
        Children.read(self)
        if ('Отличительная особенность' in self.q):
            self.power = self.q['Отличительная особенность'].value
        else: self.power = ""

    def write(self):
        Children.write(self)
        print('<td>{0}</td>'.format(self.power))
        

    def write_ch(self):
        Children.write_ch(self)
        print('<br>Отличительная особенность:<br><input type="" name="display" value="{0}">'.format(self.power))


    
    
