import cgi
from .Group import *

def main(q, selfurl):
    group=Group(q,selfurl)
    MENU = {'showgroup': group.ShowGroup,
            'addstud': group.AddStud,
            'addgrad': group.AddGrad,
            'change': group.Change,
            'edit': group.Edit,
            'delete': group.Delete,
            'clear': group.Clear}
    print ("Content-type: text/html; charset=utf-8\n\n")
  
    if 'type' in q:
        MENU[q['type'].value]()
    else:
        MENU['showgroup']()
