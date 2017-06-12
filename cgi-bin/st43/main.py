import cgi
from .container import *

def main(q, selfurl):
    group=container(q,selfurl)
    MENU = {'showgroup': group.ShowGroup,
            'addFP': group.AddFP,
            'addPFP': group.AddPFP,
            'change': group.Change,
            'edit': group.Edit,
            'delete': group.Delete,
            'clear': group.Clear}
    print ("Content-type: text/html; charset=utf-8\n\n")
  
    if 'type' in q:
        MENU[q['type'].value]()
    else:
        MENU['showgroup']()
       
