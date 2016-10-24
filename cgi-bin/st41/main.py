import cgi
from .Club import *

def main(q, selfurl):
    club=Club(q, selfurl)
    MENU = {'print_list': club.PrintList,
            'add_skater': club.AddSkater,
            'add_descendant': club.AddDescendant,
            'change': club.Change,
            'edit': club.Edit,
            'delete_element': club.DeleteElement,
            'delete_list': club.DeleteList}
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'type' in q:
        MENU[q.getvalue('type')]()
    else:
        MENU['print_list']()
