import pickle, cgi, os
from .Coming_Soon import *

class Show_Room:
    def __init__(self, q, selfurl):
        self.dealer = []
        self.q = q
        self.selfurl = selfurl

    def add_car1(self):
        self.load()
        car1 = Available_Car()
        self.dealer.append(car1)
        self.save()
        self.edit()

    def add_car2(self):
        self.load()
        car2 = Coming_Soon()
        self.dealer.append(car2)
        self.save()
        self.edit()

    def show_form(self):
        self.load()
        i = 0
        for item in self.dealer:
            print('<br>')
            item.write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<br>')
            i+=1
        print('<input type="hidden" name="student" value={0} />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="display" />')
        print('<br>')
        print('<a href={0}>Назад</a>'.format(self.selfurl))
        print('<p><a href={0}?student={1}&act=addcar1>Добавить автомобиль в наличии</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=addcar2>Добавить ожидаемый автомобиль</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))

    def get(self):
        self.load()
        self.dealer[int(self.q.getvalue('id'))].edit_car(self.q)
        self.save()
        self.show_form()

    def edit(self):
        self.load()
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        sid = str()
        if 'id' in self.q:
            sid = self.q.getvalue('id')
        else:
            sid = str(len(self.dealer)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(sid))
        print('<table>')
        self.dealer[int(sid)].show_car()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def save(self):
        pickle.dump(self.dealer, open('cgi-bin/st13/list.bin', 'wb'))

    def load(self):
        if (os.path.exists('cgi-bin/st13/list.bin')):
            self.dealer = pickle.load(open('cgi-bin/st13/list.bin', 'rb'))

    def delete(self):
        self.load()
        self.dealer.pop(int(self.q.getvalue('id')))
        self.save()
        self.show_form()

    def clear(self):
        self.load()
        self.dealer.clear()
        self.save()
        self.show_form()





