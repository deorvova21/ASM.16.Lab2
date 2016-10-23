from .group  import group
import cgi

def main(q, selfurl):
        Univer = group(q, selfurl)
        MENU = {
                'show_all': Univer.show_all,
                'badd': Univer.badd,
                'madd': Univer.madd,
                'del': Univer.delete,
                'edit': Univer.edit,
                'clear': Univer.clear
                }
        print ("Content-type: text/html; charset=utf-8\n\n")
        if 'action' in q:
                MENU[q['action'].value]()
        else:
                MENU['show_all']()


        





