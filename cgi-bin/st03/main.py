from .group import Group
import cgi

def main(q, selfurl):  

    group = Group(q, selfurl) 
    Basket = {
    '1':group.read,
    '2':group.write,
    '3':group.delete,
    '4':group.write_ch,
    '5':group.add
    }    
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'action' in q:
      Basket[q.getvalue('action')]()
    else: 
      Basket['2']()    