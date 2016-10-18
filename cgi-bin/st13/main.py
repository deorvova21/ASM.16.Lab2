from .Show_Room import *
import cgi






def main(q, selfurl):
    form = cgi.FieldStorage()
    car = Show_Room(q, selfurl)
    MENU = {
        'display': car.show_form,
        'get': car.get,
        'delete': car.delete,
        'edit': car.edit,
        'addcar1': car.add_car1,
        'addcar2': car.add_car2,
        'clear':car.clear
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
