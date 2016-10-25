from .Hero import Hero

import cgi

class Dire(Hero):
        def __init__(self, q):
                super().__init__(q)
                self.frac = ""


        def new(self):
                print('<Caption><H3>Добавление героя Dire</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q.getvalue('student')))
                print('<input type=hidden name=action value="Dadd">')
                print('<input type=hidden name=frac value="Dire">'.format(self.frac))
                print('<table border="0"><tr><td>Имя героя</td><td><input type=text name=hname value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.hname))
                print('<tr><th colspan="2">Фракция: Dire </th></tr>')
                print('<td>Сила атаки:</td><td><input type=text name=ap value="{0}"></td></tr>'.format(self.ap))
                print('<tr><td>Кол-во здоровья:</td><td><input type=text name=hp value="{0}"></td></tr>'.format(self.hp))
                print('<tr><td>Ловкость:</td><td><input type=text name=ag value="{0}"></td></tr>'.format(self.ag))
                print('<tr><td>Сила:</td><td><input type=text name=st value="{0}"></td></tr>'.format(self.st))
                print('<tr><td>Интеллект:</td><td><input type=text name=ii value="{0}"></td></tr></table>'.format(self.ii))
                print('<br> <input type=submit value="Добавить"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q.getvalue('student')))


        def add_to_table(self):
                print('<tr>')
                print('<td>{0}</td>'.format(self.hname))
                print('<td>{0}</td>'.format(self.frac))
                print('<td>{0}</td>'.format(self.ap))
                print('<td>{0}</td>'.format(self.hp))
                print('<td>{0}</td>'.format(self.ag))
                print('<td>{0}</td>'.format(self.st))
                print('<td>{0}</td>'.format(self.ii))

        def save_values(self, q):
                if 'hname' in self.q:
                        self.hname = q['hname'].value
                        if 'ap' in self.q: self.ap = q.getvalue('ap')
                        else: self.ap = ""
                        if 'hp' in self.q: self.hp = q.getvalue('hp') 
                        else: self.hp = ""
                        if 'ag' in self.q: self.ag  = q.getvalue('ag')
                        else: self.ag  = ""
                        if 'st' in self.q: self.st = q.getvalue('st')
                        else: self.st = ""
                        if 'ii' in self.q: self.ii = q.getvalue('ii')
                        else: self.ii = ""
                        if 'frac' in self.q: self.frac = q.getvalue('frac')
                        else: self.frac = ""


        def edit(self, q):
                print('<Caption><H3>Изменение героя фракции Dire</H3></Caption>')
                print('<form> <input type=hidden name=student value={0}>'.format(self.q.getvalue('student')))
                print('<input type=hidden name=action value="ee">')
                print('<input type=hidden name=id value={0}>'.format(q.getvalue('id')))
                print('<input type=hidden name=frac value="Dire">'.format(self.frac))
                print('<table border="0"><tr><td>Имя героя</td><td><input type=text name=hname value="{0}"></td><td><i>*Обязательно</i></td></tr>'.format(self.hname))
                print('<tr><th colspan="2">Фракция: Dire </th></tr>')
                print('<td>Сила атаки:</td><td><input type=text name=ap value="{0}"></td></tr>'.format(self.ap))
                print('<tr><td>Кол-во здоровья:</td><td><input type=text name=hp value="{0}"></td></tr>'.format(self.hp))
                print('<tr><td>Ловкость:</td><td><input type=text name=ag value="{0}"></td></tr>'.format(self.ag))
                print('<tr><td>Сила:</td><td><input type=text name=st value="{0}"></td></tr>'.format(self.st))
                print('<tr><td>Интеллект:</td><td><input type=text name=ii value="{0}"></td></tr></table>'.format(self.ii))
                print('<br> <input type=submit value="Сохранить изменения"> </form>')
                print('<a href="?student={0}">Вернуться к списку</a>'.format(self.q.getvalue('student')))




