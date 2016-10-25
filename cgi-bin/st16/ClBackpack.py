import pickle, cgi
from .ClAttack import *

class Backpack:
    def __init__(self, q, selfurl):
        self.list = []
        self.q = q
        self.selfurl = selfurl

    def add_pokemon(self):
        self.read_file()
        student = Pokemon()
        self.list.append(student)
        self.write_file()
        self.redact_list()

    def add_attack(self):
        self.read_file()
        attack = Attack()
        self.list.append(attack)
        self.write_file()
        self.redact_list()

    def show_list(self):
        self.read_file()
        print('<title>Список покемонов</title>\n<form>')
        print('''<table border cellspacing="0">
              <tr align="center">
              <td>Имя</td>
              <td>Тип</td>
              <td>Общий уровень</td>
              <td>Здоровье</td>
              <td>Сила атаки</td>
              <td>Сила супер-атаки</td>
              <td>Опции</td></tr>''')
        i = 0
        for item in self.list:
            print('<tr>')
            item.table_line()
            print('''<td><a href={0}?student={1}&act=redactlist&id={2}>Редактировать</a>
                  <a href={0}?student={1}&act=clearobj&id={2}>
                  Удалить</a></td></tr>'''
                  .format(self.selfurl, self.q['student'].value, i))
            i+=1
        print('</table>')
        print('<input type="hidden" name="student" value={0} />'
              .format(self.q['student'].value))
        print('<input type="hidden" name="act" id="act" value="showlist" />')
        print('<a href={0}>Назад</a>'
              .format(self.selfurl))
        print('<p><a href={0}?student={1}&act=addpokemon>Добвить покемона</a>'
              .format(self.selfurl, self.q['student'].value))
        print('<p><a href={0}?student={1}&act=addattack>Добавить покемона с известной силой</a>'
              .format(self.selfurl, self.q['student'].value))
        print('<p><a href={0}?student={1}&act=clearlist>Очистить список</a>'
              .format(self.selfurl, self.q['student'].value))
        print('</form>')

    def write_file(self):
        output = open('cgi-bin/st16/list.db', 'wb')
        pickle.dump(self.list, output)
        output.close()

    def read_file(self):
        input = open('cgi-bin/st16/list.db', 'rb')
        self.list = pickle.load(input)
        input.close()

    def get(self):
        self.read_file()
        self.list[int(self.q['id'].value)].get_value(self.q)
        self.write_file()
        self.show_list()

    def redact_list(self):
        self.read_file()
        print('<title>Изменение данных</title>\n<form>')
        print('<input type="hidden" name="student" value="{0}" />'
              .format(self.q['student'].value))
        print('<input type="hidden" name="act" value="get" />')
        p_id = str()
        if 'id' in self.q:
            p_id = self.q['id'].value
        else:
            p_id = str(len(self.list)-1)
        print('<input type="hidden" name="id" value="{0}" />'
              .format(p_id))
        print('<table>')
        self.list[int(p_id)].edit_fields()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def clear_obj(self):
        self.read_file()
        self.list.pop(int(self.q['id'].value))
        self.write_file()
        self.show_list()

    def clear_list(self):
        self.read_file()
        self.list.clear()
        self.write_file()
        self.show_list()

