from .bakalavr import bakalavr
import cgi

class magistr(bakalavr):
        def __init__(self, q):
                super().__init__(q)
                self.un   = ""
                self.prof = ""
                self.sc   = ""


        def new(self):
                print('<Caption><H3>Добавление магистра</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="madd">')
                print('<table border="0"><tr><td>ФИО студента</td><td><input type=text name=fio value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.fio))
                print('<tr><th colspan="2">Текущее образование</th><th colspan="2">Предыдущее образование</th></tr>')
                print('<td>Факультет:</td><td><input type=text name=fac value="{0}"></td>'.format(self.fac))
                print('<td>Университет:</td><td><input type=text name=un value="{0}"></td></tr>'.format(self.un))
                print('<tr><td>Курс:</td><td><input type=text name=cur value="{0}"></td>'.format(self.cur))
                print('<td>Направление:</td><td><input type=text name=prof value="{0}"></td></tr>'.format(self.prof))
                print('<tr><td>Группа:</td><td><input type=text name=gr value="{0}"></td>'.format(self.gr))
                print('<td>Средний балл:</td><td><input type=text name=sc value="{0}"></td></tr></table>'.format(self.sc))
                print('<br> <input type=submit value="Добавить"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q['student'].value))


        def add_to_table(self):
                print('<tr>')
                print('<td>{0}</td>'.format(self.fio))
                print('<td>{0}</td>'.format(self.fac))
                print('<td>{0}</td>'.format(self.cur))
                print('<td>{0}</td>'.format(self.gr))
                print('<td>{0}</td>'.format(self.un))
                print('<td>{0}</td>'.format(self.prof))
                print('<td>{0}</td>'.format(self.sc))

        def save_values(self, q):
                if 'fio' in self.q:
                        self.fio = q['fio'].value
                        if 'fac' in self.q: self.fac = q['fac'].value
                        else: self.fac = ""
                        if 'cur' in self.q: self.cur = q['cur'].value 
                        else: self.cur = ""
                        if 'gr' in self.q: self.gr  = q['gr'].value
                        else: self.gr  = ""
                        if 'un' in self.q: self.un = q['un'].value
                        else: self.un = ""
                        if 'prof' in self.q: self.prof = q['prof'].value
                        else: self.prof = ""
                        if 'sc' in self.q: self.sc = q['sc'].value
                        else: self.sc = ""

        def edit(self, q):
                print('<Caption><H3>Изменение магистра</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="edit">')
                print('<input type=hidden name=id value={0}>'.format(q['id'].value))
                print('<table border="0"><tr><td>ФИО студента</td><td><input type=text name=fio value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.fio))
                print('<tr><th colspan="2">Текущее образование</th><th colspan="2">Предыдущее образование</th></tr>')
                print('<td>Факультет:</td><td><input type=text name=fac value="{0}"></td>'.format(self.fac))
                print('<td>Университет:</td><td><input type=text name=un value="{0}"></td></tr>'.format(self.un))
                print('<tr><td>Курс:</td><td><input type=text name=cur value="{0}"></td>'.format(self.cur))
                print('<td>Направление:</td><td><input type=text name=prof value="{0}"></td></tr>'.format(self.prof))
                print('<tr><td>Группа:</td><td><input type=text name=gr value="{0}"></td>'.format(self.gr))
                print('<td>Средний балл:</td><td><input type=text name=sc value="{0}"></td></tr></table>'.format(self.sc))
                print('<br> <input type=submit value="Сохранить изменения"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q['student'].value))



