from .dancer import *

class Soloist (Dancer):

    def __init__(self):
        super().__init__()
        self.time = ''
        self.best_performance = ''
        self.bonus = ''

    def identification(self, q):
        super().identification(q)
        self.time = q.getvalue('time')
        self.best_performance = q.getvalue('best_performance')
        self.bonus = q.getvalue('bonus')

    def indicate(self):
        print('<TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD><TD>{}</TD>'.format(self.name, self.age, self.period, self.time, self.title, self.best_performance, self.bonus))

    def point_out(self):
        super().point_out()
        print("""<TR><TH>Стаж в качестве солиста</TH><TD><input type="text"name="time" value="{}"></TD></TR>
<TR><TH>Лучшие постановки с участием солиста</TH><TD><input type="text"name="best_performance" value="{}"></TD></TR>
<TR><TH>Размер премии</TH><TD><input type="text"name="bonus" value="{}"></TD></TR>""".format(self.time, self.best_performance, self.bonus))


