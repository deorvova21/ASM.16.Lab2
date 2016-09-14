import cgi
def exec_delete(studnum,group, q, selfurl):
    try:
        int(studnum)
        group.check(int(studnum)-1)
        group.delete(int(studnum)-1)
        group.save()
        print(group)
        print ('<br><a href="{0}">Назад</a> | <a href="{0}?student={1}&choice=1">Добавить</a>'.format(selfurl, q['student'].value))
    except (ValueError, IndexError):
        print("Invalid selection!\n")
        delete(group)
    return

def delete(group, q, selfurl):
    if len(group) < 1:
        print("List empty\n")
    else:
        form = cgi.FieldStorage()
        studnum = form.getfirst("num", None)
        if studnum is not None:
            exec_delete(studnum,group, q, selfurl)
    return