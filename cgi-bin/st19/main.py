from .group import group
import cgi

def main(q, selfurl):
        company=group(q,selfurl)
        MENU = {
                'show_list': company.show_list,
                'add_emploee': company.add_emploee,
                'add_chief': company.add_chief,
                'delete_obj':company.delete_obj,
                'save_form':company.save_form,
                'edit':company.edit,
                'clear_list': company.clear_list
                }
        print ("Content-type: text/html; charset=utf-8\n\n")
        if 'action' in q:
                MENU[q['action'].value]()
        else:
                MENU['show_list']()
 
