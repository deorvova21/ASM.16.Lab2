import cgi

class bakalavr:

        def __init__(self, q):
                self.q = q
                self.fio = ""
                self.fac = ""
                self.cur = ""
                self.gr = ""

        def new(self): 
                print('<Caption><H3>Добавление бакалавра</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="badd">')
                print('<table border="0"><tr><td>ФИО студента:</td><td><input type=text name=fio value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.fio))
                print('<tr><td>Факультет:</td><td><input type=text name=fac value="{0}"></td></tr>'.format(self.fac))
                print('<tr><td>Курс:</td><td><input type=text name=cur value="{0}"></td></tr>'.format(self.cur))
                print('<tr><td>Группа:</td><td><input type=text name=gr value="{0}"></td></tr></table>'.format(self.gr))
                print('<br><input type=submit value="Добавить"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q['student'].value))


        def add_to_table(self):
                print('<tr>')
                print('<td>{0}</td>'.format(self.fio))
                print('<td>{0}</td>'.format(self.fac))
                print('<td>{0}</td>'.format(self.cur))
                print('<td>{0}</td>'.format(self.gr))
                print('<th colspan="3">Нет (бакалавр)</th>')

        def save_values(self, q):
                if 'fio' in self.q:
                        self.fio = q.getvalue('fio')
                        if 'fac' in self.q: self.fac = q.getvalue('fac')
                        else: self.fac = ""
                        if 'cur' in self.q: self.cur = q.getvalue('cur')
                        else: self.cur = ""
                        if 'gr' in self.q: self.gr  = q.getvalue('gr')
                        else: self.gr  = ""


        def edit(self, q):
                print('<Caption><H3>Изменение бакалавра</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
                print('<input type=hidden name=action value="end_edit">')
                print('<input type=hidden name=id value={0}>'.format(q['id'].value))
                print('<table border="0"><tr><td>ФИО студента:</td><td><input type=text name=fio value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.fio))
                print('<tr><td>Факультет:</td><td><input type=text name=fac value="{0}"></td></tr>'.format(self.fac))
                print('<tr><td>Курс:</td><td><input type=text name=cur value="{0}"></td></tr>'.format(self.cur))
                print('<tr><td>Группа:</td><td><input type=text name=gr value="{0}"></td></tr></table>'.format(self.gr))
                print('<br><input type=submit value="Сохранить изменения"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q['student'].value))

        
