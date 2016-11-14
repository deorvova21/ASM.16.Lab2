from .products import Products
import cgi

class Vegetables(Products):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.q=q
        self.selfurl=selfurl
        self.potatoe =""
        self.cabbage =""
        self.carrot =""
        self.peas =""
        self.parsley =""
        self.blette =""

    def read(self, q):
        self.q=q
        Products.read(self, q)
        if ('potatoe' in self.q):
            self.potatoe = self.q['potatoe'].value
        else: self.potatoe = ""
        if ('cabbage' in self.q):
            self.cabbage = self.q['cabbage'].value
        else: self.cabbage = ""
        if ('carrot' in self.q):
            self.carrot = self.q['carrot'].value
        else: self.carrot = ""
        if ('peas' in self.q):
            self.peas = self.q['peas'].value
        else: self.parsley = ""
        if ('parsley' in self.q):
            self.parsley = self.q['parsley'].value
        else: self.parsley = ""
        if ('blette' in self.q):
            self.blette = self.q['blette'].value
        else: self.blette = ""
       
    def write(self):
       Products.write(self)
       #print('<br>{0}</br>'.format(self.potatoe))
       #print('<br>{0}</br>'.format(self.cabbage))
       #print('<br>{0}</br>'.format(self.carrot))
       #print('<br>{0}</br>'.format(self.peas))
       #print('<br>{0}</br>'.format(self.parsley))
       #print('<br>{0}</br>'.format(self.blette))
       print("""
        <TR><TH>Картошка</TH><TD>{0}</TD></TR>
<TR><TH>Капуста</TH><TD>{1}</TD></TR>
<TR><TH>Морковка</TH><TD>{2}</TD>
<TR><TH>Горох</TH><TD>{3}</TD>
<TR><TH>Петрушка</TH><TD>{4}</TD>
<TR><TH>и Свекла</TH><TD>{5}</TD>
</TR>""".format(self.potatoe, self.cabbage, self.carrot, self.parsley, self.peas, self.blette))

        

    def write_ch(self, q):
        Products.write_ch(self, q)
        #print('<br>Potatoe:<br><input type="text" name="potatoe" value="{0}">'.format(self.potatoe))
        #print('<br>Cabbage:<br><input type="text" name="cabbage" value="{0}">'.format(self.cabbage))
        #print('<br>Carrot:<br><input type="text" name="carrot" value="{0}">'.format(self.carrot))
        #print('<br>Peas:<br><input type="text" name="peas" value="{0}">'.format(self.parsley))
        #print('<br>Parsley:<br><input type="text" name="parsley" value="{0}">'.format(self.peas))
        #print('<br>Blette:<br><input type="text" name="blette" value="{0}">'.format(self.blette))
        print("""<TR><TH>Картошка</TH><TD><input type="text"name="potatoe" value="{0}"></TD></TR>
<TR><TH>Капуста</TH><TD><input type="text"name="cabbage" value="{1}"></TD></TR>
<TR><TH>Морковка</TH><TD><input type="text"name="carrot" value="{2}"></TD>
<TR><TH>Горох</TH><TD><input type="text"name="parsley" value="{3}"></TD>
<TR><TH>Петрушка</TH><TD><input type="text"name="peas" value="{4}"></TD>
<TR><TH>и Свекла</TH><TD><input type="text"name="blette" value="{5}"></TD>
</TR>""".format(self.potatoe, self.cabbage, self.carrot, self.parsley, self.peas, self.blette))
     

        
                
                
       