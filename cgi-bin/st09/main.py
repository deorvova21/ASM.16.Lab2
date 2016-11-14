import cgi
from .group import *
from .student import *

def main(q,selfurl):
        Group=group(q,selfurl)
        MYMENU = {
                'showstudents': Group.showstudents,
                'studentform' : Group.studentform,
                'addstudent' : Group.addstudent,
                'starostaform' : Group.starostaform,
                'addstarosta' : Group.addstarosta,
                'deletestudent': Group.delete,
                'editform' : Group.editform,
                'edit' : Group.edit,
                'clear' : Group.clear,
                'savefile': Group.writef,
                'loadfile': Group.readf,
                }

        print ("Content-type: text/html; charset=utf-8\n\n")
  
        if 'type' in q:
                MYMENU[q['type'].value]()
        else:
                MYMENU['showstudents']()

