from .group import *
import cgi

def main(q, selfurl):
        Gr = Group(q, selfurl)
        print ("Content-type: text/html; charset=utf-8\n\n")
        if 'action' in q:
                if (q['action'].value=="1"): 
                        Gr.write()
                if (q['action'].value=="2"): 
                        Gr.read()
                if (q['action'].value=="3"):
                        Gr.add()
                if (q['action'].value=="4"):
                        Gr.delete()
        else:
                Gr.write()




                
                        
                
                        
