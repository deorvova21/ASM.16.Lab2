import pickle, os
from .soloist import *

class Troupe:
    
    def __init__(self, q, selfurl):
        self.dancers = []
        self.q = q
        self.selfurl = selfurl
        
    def screen(self):
        self.load()
        print("""<TITLE>Труппа</TITLE><FORM>
<H1> <P ALIGN = "CENTER"><B><FONT FACE = "Times new rouman" COLOR = "Green"> Список труппы </P></H1>
<TABLE BORDER = "1" CELLSPACING = "0">
<COL SPAN = "7" STYLE = "background:LightCyan">
<COL STYLE = "background-color:Khaki">
<TR><TH>Имя</TH><TH>Возраст</TH><TH>Стаж в труппе</TH><TH>Стаж солиста</TH><TH>Наличие званий</TH><TH>Лучшие постановки</TH><TH>Премия</TH><TH>Опции</TH></TR>""")
        i =0
        for item in self.dancers:
            print('<TR>')
            item.indicate()
            print('<TD><A href={0}?student={1}&act=redact&id={2}>Изменить</A><A href={0}?student={1}&act=delete_member&id={2}>Удалить</A></TD></TR>'.format(self.selfurl, self.q.getvalue('student'), i))
            i+=1
        print("""</TABLE>
<input type="hidden" name="student" value={0} />
<input type="hidden" name="act" value="screen" />
<input type="hidden" name="id" id="id" value="0" />
<A href={1}>Назад</A>
<P><A href={1}?student={0}&act=plus_dancer>Добавить танцора</A>   или   <A href={1}?student={0}&act=plus_soloist>Добавить солиста</A>
<P><A href={1}?student={0}&act=clear_trope>Очистить список труппы</A>

</FORM>""".format(self.q.getvalue('student'), self.selfurl))

    def get(self):
        self.load()
        self.dancers[int(self.q.getvalue('id'))].identification(self.q)
        self.save()
        self.screen()

    def plus_dancer(self):
        self.load()
        dancer = Dancer()
        self.dancers.append(dancer)
        self.save()
        self.redact()

    def plus_soloist(self):
        self.load()
        soloist = Soloist()
        self.dancers.append(soloist)
        self.save()
        self.redact()

    def redact(self):
        self.load()
        print("""<TITLE>Труппа</TITLE>\n<FORM>
<input type="hidden" name="student" value="{}" />
<input type="hidden" name="act" value="get" />""".format(self.q.getvalue('student')))
        sid = str()
        if 'id' in self.q:
            sid = self.q.getvalue('id')
        else:
            sid = str(len(self.dancers)-1)
        print('<input type="hidden" name="id" value="{}" />'.format(sid))
        print('<TABLE>')
        self.dancers[int(sid)].point_out()
        print('</TABLE> <P></P>')
        print('<input type="submit" value="Сохранить изменения"></FORM>')

    def delete_member(self):
        self.load()
        self.dancers.pop(int(self.q.getvalue('id')))
        self.save()
        self.screen()

    def clear_troupe(self):
        self.load()
        self.dancers.clear()
        self.save()
        self.screen()

    def save(self):
        pickle.dump(self.dancers, open('cgi-bin/st24/troupe.dat', 'wb'))

    def load(self):
        if (os.path.exists('cgi-bin/st40/list.bin')):
            self.dancers = pickle.load(open('cgi-bin/st24/troupe.dat', 'rb'))
        
