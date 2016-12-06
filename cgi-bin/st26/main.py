from .container import *
import cgi

def main(q, selfurl):
    form = cgi.FieldStorage()
    cont = container(q, selfurl)
    MENU = {
        'showList': cont.showList,
        'get': cont.get,
        'deleteObj': cont.deleteObj,
        'edit': cont.editObj,
        'addClass1': cont.addClass1,
        'addClass2': cont.addClass2,
        'clearList': cont.clearList
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['showList']()

