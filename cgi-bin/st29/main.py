import cgi
from .group import *

def main(q, selfurl):
    group=Group(q,selfurl)
    MENU = {'Display': group.Display,
            'AddStud':  group.AddStudent,
            'AddStudForm':  group.AddStudentForm,
            'AddStar':  group.AddStarosta,
            'AddStarForm':  group.AddStarostaForm,
            'EditForm':  group.EditForm,
            'Edit':  group.Edit,
            'Delete':  group.Delete,
            'Clear':  group.Clear}
    print ("Content-type: text/html; charset=utf-8\n\n")
    if 'type' in q:
        MENU[q['type'].value]()
    else:
        MENU['Display']()

