from .Phone import *
import cgi

class Smartphone(Phone):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.os=""
        self.os_ver=""
        self.q=q
        self.selfurl=selfurl
    
    def read(self):
        Phone.read(self)
        if ('os' in self.q):
            self.os = self.q['os'].value
        else:
            self.os = ''
        if ('os_ver' in self.q):
            self.os_ver = self.q['os_ver'].value
        else:
            self.os_ver = ''
        
    def show_form(self):
        Phone.show_form(self)
        print('<table>')
        print('<td align="right" width="100">Название ОС</td><td><input type="text" name="os" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.os))
        print('<td align="right" width="100">Версия ОС</td><td><input type="text" name="os_ver" value="{0}" maxlength="50" size="20"></td></tr>'.format(self.os_ver))
                
    def show_values(self):
        Phone.show_values(self)
        print('<td>{0}</td>'.format(self.os))
        print('<td>{0}</td>'.format(self.os_ver))
    
    
