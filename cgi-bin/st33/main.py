from st33.contASM import *
import cgi

def main(q, selfurl): 
    group = ASM(q, selfurl) 
    menu_actions = {
    #'1': group.add,
    '2': group.edit,
    '1': group.delete
    }
    print(LoadTpl('main').format(selfurl, q['student'].value))
    choice = q.getfirst("choice", None)
    try:
        group.readf()
    except (FileNotFoundError):
        group.writef()
        group.readf()
    if choice is not None:
        menu_actions[choice](q, selfurl) 
    group.show(q, selfurl)
    print(LoadTpl('footer'))    
    
if __name__=="__main__":
    main()
