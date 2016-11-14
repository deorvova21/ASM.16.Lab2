from .products import Products
import cgi

class Fruits(Products):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.apples=""
        self.pineapples=""
        self.peaches=""
        self.plums=""
        self.q=q
        self.selfurl=selfurl
    
    def read(self, q):
        self.q = q
        Products.read(self, q)
        if ('apples' in self.q):
            self.apples = self.q['apples'].value
        else: self.apples = ""
        if ('pineapples' in self.q):
            self.pineapples = self.q['pineapples'].value
        else: self.pineapples = ""
        if ('peaches' in self.q):
            self.peaches = self.q['peaches'].value
        else: self.peaches = ""
        if ('plums' in self.q):
            self.plums = self.q['plums'].value
        else: self.plums = ""

    def write(self):
        Products.write(self)
        #print('<br>{0}</br>'.format(self.apples))
        #print('<br>{0}</br>'.format(self.pineapples))
        #print('<br>{0}</br>'.format(self.peaches))
        #print('<br>{0}</br>'.format(self.plums))
        print("""<TR><TH>Яблоки</TH><TD>{0}</TD></TR>
<TR><TH>Ананасы</TH><TD>{1}</TD></TR>
<TR><TH>Персики</TH><TD>{2}</TD>
<TR><TH>Сливы лиловые, спелые, садовые</TH><TD>{3}</TD>
</TR>""".format(self.apples, self.pineapples, self.peaches, self.plums))

    def write_ch(self, q):
        Products.write_ch(self, q)
        #print('<br>Apples:<br><input type="text" name="apples" value="{0}">'.format(self.apples))
        #print('<br>Pineapples:<br><input type="text" name="pineapples" value="{0}">'.format(self.pineapples))
        #print('<br>Peaches:<br><input type="text" name="peaches" value="{0}">'.format(self.peaches))
        #print('<br>Plums:<br><input type="text" name="plums" value="{0}">'.format(self.plums))
        print("""<TR><TH>Яблоки</TH><TD><input type="text"name="apples" value="{0}"></TD></TR>
<TR><TH>Ананасы</TH><TD><input type="text"name="pineapples" value="{1}"></TD></TR>
<TR><TH>Персики</TH><TD><input type="text"name="peaches" value="{2}"></TD>
<TR><TH>Сливы, лиловые, спелые, садовые</TH><TD><input type="text"name="plums" value="{3}"></TD>
</TR>""".format(self.apples, self.pineapples, self.peaches, self.plums))
