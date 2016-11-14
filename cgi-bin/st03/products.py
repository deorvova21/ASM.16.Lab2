import cgi
class Products:
    def __init__(self, q, selfurl):
    	self.q=q
    	self.name=""

    def read(self, q):
    	self.q = q
    	if ('name' in self.q):
    		self.name = self.q['name'].value
    	else: self.name=""
        
    def write_ch(self, q):
        self.q=q
        print("""<H2> <P ALIGN="CENTER"><B><FONT FACE="Times new roman" COLOR="Green"> Продукты </P></H2> 
<H4> <P ALIGN="CENTER"><FONT FACE="Times new rouman" COLOR="Green"> (Выполните выбранное действие: добавление продукта(овощи/фрукты)) </P></H4>
<TABLE BORDER="1" CELLSPACING="0">
<COL SPAN = "2" STYLE = "background:LightCyan"></TD><TR>""")
        print('<form action="{0}?student={1}&action=1&type=3&id={2}&add={3}">'.format(self.selfurl, self.q['student'].value, self.q['id'].value, self.q['type'].value))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(self.q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("1"))
        print('<input type="text" name="type" value="{0}" style="display:none">'.format("3"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(self.q['id'].value))
        print('<input type="text" name="add" value="{0}" style="display:none">'.format(self.q['type'].value))
        print('<TR><TH>Имя</TH><TD><input type="text" name="name" value="{0}"></TD></TR>'.format(self.name))
       

    def write(self):
        print("""<H2> <P ALIGN="CENTER"><B><FONT FACE="Times new roman" COLOR="Green">Продукты</P></H2> 
<H4> <P ALIGN="CENTER"><FONT FACE="Times new rouman" COLOR="Green"></P></H4>
<TABLE BORDER="1" CELLSPACING="0">
<COL SPAN = "2" STYLE = "background:LightCyan"></TD><TR>""")
        print("<TR><TH>Имя</TH><TD>{0}</TD></TR>".format(self.name))
        
        

    