import cgi

class Pokemon:
    def __init__(self, q):
        self.q = q
        self.name = ''
        self.poktype = ''
        self.cp = ''
        self.hp = ''

    def table_line(self):
        print('''<td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
                 <td>{4}</td>
                 <td>{5}</td>'''
              .format(self.name, self.poktype, self.cp, self.hp, '--', '--'))

    def edit_fields(self):
        print('''<tr><p><td>Имя:</td>
              <td><input type="text" name="name" value="{0}"></td></tr>'''
              .format(self.name))
        print('''<tr><p><td>Тип:</td><td><input type="text" name="poktype"
              value="{0}"></td></tr>'''
              .format(self.poktype))
        print('''<tr><p><td>Общий уровень:</td><td><input type="text" name="cp"
              value="{0}"></td></tr>'''
              .format(self.cp))
        print('''<tr><p><td>Здоровье:</td><td><input type="text" name="hp"
              value="{0}"></td></tr>'''
              .format(self.hp))
        
    def get_value(self, q):
        self.name = q.getvalue('name')
        self.poktype = q.getvalue('poktype')
        self.cp = q.getvalue('cp')
        self.hp = q.getvalue('hp')

    def get_value_for_add(self, q):
        if 'name' in self.q:    
            self.name = q.getvalue('name')
        else:
            self.name = ' '
        if 'poktype' in self.q:
            self.poktype = q.getvalue('poktype')
        else:
            self.poktype = ' '
        if 'cp' in self.q:
            self.cp = q.getvalue('cp')
        else:
            self.cp = ' '
        if 'hp' in self.q:
            self.hp = q.getvalue('hp')
        else:
            self.hp = ' '

    
