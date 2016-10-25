import cgi

class Pokemon:
    def __init__(self):
        self.name=''
        self.poktype=''
        self.cp=''
        self.hp=''

    def table_line(self):
        print('''<td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
                 <td>{4}</td>
                 <td>{5}</td>'''
              .format(self.name, self.poktype, self.cp, self.hp, '--', '--'))

    def edit_fields(self):
        print('''<tr><td>Имя:</td>
              <td><input type="text" name="name" value="{0}"></td></tr>'''
              .format(self.name))
        print('''<tr><td>Тип:</td><td><input type="text" name="poktype"
              value="{0}"></td></tr>'''
              .format(self.poktype))
        print('''<tr><td>Общий уровень:</td><td><input type="text" name="cp"
              value="{0}"></td></tr>'''
              .format(self.cp))
        print('''<tr><td>Здоровье:</td><td><input type="text" name="hp"
              value="{0}"></td></tr>'''
              .format(self.hp))
        
    def get_value(self, q):
        self.name = q.getvalue('name')
        self.poktype = q.getvalue('poktype')
        self.cp = q.getvalue('cp')
        self.hp = q.getvalue('hp')
