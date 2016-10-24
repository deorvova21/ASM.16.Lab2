from .group  import group
import cgi

def main(q, selfurl):
        Hero = group(q, selfurl)
        MENU = {
                'show_all': Hero.show_all,
                'Dadd': Hero.Dadd,
                'Radd': Hero.Radd,
                'del': Hero.delete,
                'edit': Hero.edit,
                'clear': Hero.clear
                }
        print ("Content-type: text/html; charset=utf-8\n\n")
        if 'action' in q:
                MENU[q['action'].value]()
        else:
                MENU['show_all']()

