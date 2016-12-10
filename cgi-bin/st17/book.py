from .tpl import *

class book(object):
    def __init__(self):
        self.name = ""
        self.year = ""
        self.location = ""

    def inputing(self, q):
        if 'location' in q:
            self.location = q['location'].value
        else: self.location = ""
        if 'name' in q:
            self.name = q['name'].value
        else: self.name = ""
        if 'year' in q:
            self.year = q['year'].value
        else: self.year = ""
                    
    def printing(self, id, q, selfurl):
        print('<tr><td width=100> Book </td><td width=150> {0} </td>'.format(self.name))
        print('<td> {0} </td>'.format(self.year))
        print('<td>  </td><td>  </td><td> {0} </td>'.format(self.location))
        print('''<td>
<a href="{0}?student={1}&action=6&id={2}">Change element</a> <br> <a href="{0}?student={1}&action=7&id={2}">Delete element</a></td></tr>'''.format(selfurl, q['student'].value, id))

    def change(self, id, q, selfurl):
        print('''
<p align=center><font color=#800000 size=6>
Please, enter information about Book:
</font> </p>
''')
        print(load('block'))
        print('<div class="block">')
        print('<form action="{0}" method="get">'.format(selfurl))
        print('<input type="text" name="student" value="{0}" style="display:none">'.format(q['student'].value))
        print('<input type="text" name="action" value="{0}" style="display:none">'.format("4"))
        print('<input type="text" name="id" value="{0}" style="display:none">'.format(id))
        print('Name:<br><input type="text" name="name" value="{0}"><br>'.format(self.name))
        print('Year:<br><input type="text" name="year" value="{0}"><br>'.format(self.year))
        print('Location:<br><input type="text" name="location" value="{0}"><br>'.format(self.location))
        print('<br><br><a href="{0}?student={1}">Cancel </a>&emsp;<input type="submit" value="Save"></form>'.format(selfurl, q['student'].value))
        print('</div>')
