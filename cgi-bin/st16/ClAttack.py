from .ClPokemon import *

class Attack(Pokemon):
    def __init__(self):
        super().__init__()
        self.attack=''
        self.superattack=''
    
    def table_line(self):
        print('''<td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
                 <td>{4}</td>
                 <td>{5}</td>'''
              .format(self.name, self.poktype, self.cp, self.hp, self.attack, self.superattack))

    def edit_fields(self):
        super().edit_fields()
        print('''<tr><td>Сила атаки:</td><td><input type="text"
              name="attack" value="{0}"></td></tr>'''
              .format(self.attack))
        print('''<tr><td>Сила-супер-атаки:</td><td><input type="text"
              name="superattack" value="{0}"></td></tr>'''
              .format(self.superattack))

    def get_value(self, q):
        super().get_value(q)
        self.attack = q.getvalue('attack')
        self.superattack = q.getvalue('superattack')
