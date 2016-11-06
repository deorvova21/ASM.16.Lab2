from .spisok import *
import cgi

def main(q, selfurl):
        
        Sp=Spisok(q, selfurl)
        print ("Content-type: text/html; charset=utf-8\n\n")
        if 'action' in q:
                if (q['action'].value=="1"): 
                        Sp.change()
                if (q['action'].value=="2"): 
                        Sp.read()
                if (q['action'].value=="3"):
                        Sp.delete()
        else:
                Sp.write()
                        
                
                        
