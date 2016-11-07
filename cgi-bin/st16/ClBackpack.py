import pickle, cgi
from .ClAttack import *

class Backpack:
    def __init__(self, q, selfurl):
        self.list = []
        self.q = q
        self.selfurl = selfurl
        
    def add_pokemon(self):
        pokemon = Pokemon(self.q)
        self.read_file()
        self.list.insert(0, pokemon)
        print('<form><input type=hidden name=student value={0}>'.format(self.q['student'].value))
        print('<input type=hidden name=act value="addpokemon">')
        pokemon.edit_fields()
        pokemon.get_value_for_add(self.q)
        print('<p><input type="submit" value="Сохранить"></form>')
        print('<p><a href="?student={0}">Скрыть форму</a>'.format(self.q['student'].value))
        if pokemon.name != ' ' and pokemon.poktype != ' ' and pokemon.cp != ' ' and pokemon.hp != ' ':
            self.write_file()
        self.show_list()
        
    def add_attack(self):
        attack = Attack(self.q)
        self.read_file()
        self.list.insert(0, attack)
        print('<form> <input type=hidden name=student value={0}>'.format(self.q['student'].value))
        print('<input type=hidden name=act value="addattack">')
        attack.edit_fields()
        attack.get_value_for_add(self.q)
        print('<p><input type="submit" value="Сохранить"></form>')
        print('<p><a href="?student={0}">Скрыть форму</a>'.format(self.q['student'].value))
        if attack.name != ' ' and attack.poktype != ' ' and attack.cp != ' ' and attack.hp != ' ' and attack.attack != ' ' and attack.superattack != ' ':
            self.write_file()
        self.show_list()

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
        print('''<p><a href={0}?student={1}&act=addpokemon>Добвить покемона</a>
        <p><a href={0}?student={1}&act=addattack>Добавить покемона с известной силой</a>
        <p><a href={0}?student={1}&act=clearlist>Очистить список</a>'''
              .format(self.selfurl, self.q['student'].value))
        print('</form>')

    def write_file(self):
        output = open('cgi-bin/st16/list.db', 'wb')
        pickle.dump(self.list, output)
        output.close()

    def read_file(self):
        iinput = open('cgi-bin/st16/list.db', 'rb')
        self.list = pickle.load(iinput)
        iinput.close()

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
        print('<input type="hidden" name="id" value="{0}" />'
              .format(self.q['id'].value))
        print('<table>')
        self.list[int(self.q['id'].value)].edit_fields()
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

