from .troupe import *

def main(q, selfurl):
    troupe =Troupe(q,selfurl)
    MENU = {
        'screen': troupe.screen,
        'get':troupe.get,
        'plus_dancer':troupe.plus_dancer,
        'plus_soloist':troupe.plus_soloist,
        'redact':troupe.redact,
        'delete_member':troupe.delete_member,
        'clear_trope':troupe.clear_troupe
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q.getvalue('act')]()
    else:
        MENU['screen']()
