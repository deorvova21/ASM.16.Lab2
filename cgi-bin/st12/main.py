from .car_company import *
import cgi


def main(q, selfurl):
    form = cgi.FieldStorage()
    car = Car_company(q, selfurl)
    MENU = {
        'display': car.print_all,
        'get': car.get,
        'delete': car.delete,
        'edit': car.edit,
        'add_car_company': car.add_car_company,
        'add_driver_company': car.add_driver_company,
        'clear':car.clear
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
