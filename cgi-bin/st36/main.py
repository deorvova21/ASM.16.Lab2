from .Music import *
import cgi

def main(q, selfurl):
    OP = Music(q, selfurl)
    OP.Load()
    MENU = {
        'display': OP.ShowList,
        'get': OP.Get,
        'delete': OP.Delete,
        'edit': OP.Edit,
        'addnative': OP.AddNative,
        'addforeign': OP.AddForeign,
        'clear': OP.Clear
    }
    print("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['display']()
    OP.Save()
