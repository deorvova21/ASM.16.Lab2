import cgi
from .University import *

def main(q, selfurl):
    university=University(q,selfurl)
    MENU = {'showform': university.ShowSpisok,
            'add_stu': university.new_stu,
            'add_sta': university.new_sta,
            'change': university.change,
            'edit': university.edit,
            'dell': university.dell,
            'dell_all': university.dell_all}
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'type' in q:
        MENU[q['type'].value]()
    else:
        MENU['showform']()
