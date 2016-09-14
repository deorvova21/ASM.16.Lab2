from .group import *
from .add_function import *
from .delete_function import *
from .edit_function import *
from .load_function import *
from .print_function import *
from .save_function import *
import cgi


def main(q, selfurl): 
    group = Group(q, selfurl)  
    print ("Content-type: text/html; charset=utf-8\n\n")
    
    form = cgi.FieldStorage()
    try:
        menu_actions['6'](group) #загрузка 
    except (FileNotFoundError):
        group.add(Student(None,None,None,None))
        menu_actions['5'](group)
        menu_actions['6'](group)    
    choice = form.getfirst("choice", None)
    if choice != str(1) and choice != str(2) and choice != str(3):
        menu_actions['4'](group) #вывод
        print ('<br><a href="{0}">Назад</a> | <a href="{0}?student={1}&choice=1">Добавить</a>'.format(selfurl, q['student'].value)) 
    if choice is not None:
        exec_menu(choice, q, selfurl, group)

def exec_menu(choice, q, selfurl, group):
    try:
        menu_actions[choice](group, q, selfurl)
    except KeyError:
        print("Invalid selection!\n")
    # if choice != '0':       
        # menu_actions['main'](q, selfurl)


menu_actions = {
    'main': main,
    '1': add,
    '2': edit,
    '3': delete,
    '4': print_list,
    '5': save,
    '6': load
}
 
if __name__ == "__main__":
    main()