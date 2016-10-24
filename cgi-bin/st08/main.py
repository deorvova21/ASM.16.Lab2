from .func import *
import cgi

def main(q, selfurl):
        print ("Content-type: text/html; charset=utf-8\n\n")
        funct=functions(q, selfurl)
        MENU = {'showform': funct.showform,
                'doadd_bud': funct.doadd_bud,
                'doadd_comm': funct.doadd_comm,
                'delete': funct.dodel,
                'edit': funct.edit,
                'gett': funct.gett}

        funct.load()
        if 'act' in q:
                MENU[q['act'].value]()
        else:
                MENU['showform']()
        funct.save()
