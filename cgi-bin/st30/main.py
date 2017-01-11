from .list import *
import cgi

def main(q, selfurl):
    _list = List(q, selfurl)
    _list.Load()
    MENU = {
        'display': _list.ShowList,
        'get': _list.Get,
        'delete': _list.Delete,
        'edit': _list.Edit,
        'addfree': _list.AddFree,
        'addcontract': _list.AddContract,
        'clear': _list.Clear
    }
    print("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
    _list.Save()
