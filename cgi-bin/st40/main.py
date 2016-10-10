from .clist import *
import cgi

def main(q, selfurl):
    form = cgi.FieldStorage()
    _list = List(q, selfurl)
    MENU = {
        'display': _list.display,
        'get': _list.get,
        'delete': _list.delete,
        'edit': _list.edit,
        'addstudent': _list.add_student,
        'addelder': _list.add_elder,
        'clear': _list.clear
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
