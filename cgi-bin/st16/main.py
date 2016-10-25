from .ClBackpack import *
import cgi

def main(q, selfurl):
    form = cgi.FieldStorage()
    backpack = Backpack(q, selfurl)
    MENU = {
        'showlist': backpack.show_list,
        'get': backpack.get,
        'clearobj': backpack.clear_obj,
        'redactlist': backpack.redact_list,
        'addpokemon': backpack.add_pokemon,
        'addattack': backpack.add_attack,
        'clearlist': backpack.clear_list
    }
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'act' in q:
        MENU[q['act'].value]()
    else:
        MENU['showlist']()
