class Dancer:

    def __init__(self):
        self.name = ''
        self.age = ''
        self.period = '' 
        self.title = ''

    def indicate(self):
        print('<TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD>'.format(self.name, self.age, self.period, 'только для солистов', self.title, 'только для солистов', 'только для солистов'))

    def point_out(self):
        print("""<H2> <P ALIGN="CENTER"><B><FONT FACE="Times new rouman" COLOR="Green"> Редактирование состава труппы </P></H2> 
<H4> <P ALIGN="CENTER"><FONT FACE="Times new rouman" COLOR="Green"> (Выполните выбранное действие: добавление участника(танцора/солиста), изменение данных участника труппы) </P></H4>
<TABLE BORDER="1" CELLSPACING="0">
<COL SPAN = "2" STYLE = "background:LightCyan">
<TR><TH>Имя</TH><TD><input type="text"name="name" value="{}"></TD></TR>
<TR><TH>Возраст</TH><TD><input type="text"name="age" value="{}"></TD></TR>
<TR><TH>Стаж работы в труппе</TH><TD><input type="text"name="period" value="{}"></TD></TR>
<TR><TH>Имеющиеся звания</TH><TD><input type="text"name="title" value="{}"></TD></TR>""".format(self.name, self.age, self.period, self.title))
    
    def identification(self, q): 
       self.name = q.getvalue('name')
       self.age = q.getvalue('age')
       self.period = q.getvalue('period')
       self.title = q.getvalue('title')    
