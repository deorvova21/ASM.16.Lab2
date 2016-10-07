import cgi
from .student import *
from .monitor import *
def exec_edit(studnum,group, q, selfurl, student):
    try:
        int(studnum)
        group.check(int(studnum)-1)
        group.edit(int(studnum)-1, student)
        group.save()
        print ('<br><a href="{0}?student={1}">Назад</a>'.format(selfurl, q['student'].value))
    except (ValueError, IndexError):
        print("Invalid selection!\n")
        edit(group)
    return

def edit(group, q, selfurl):
    if len(group) < 1:
        print("List empty\n")
    else:
        studnum = q.getfirst("num", None)
        name = q.getfirst("name", group.getName(int(studnum)-1))
        age = q.getfirst("age", group.getAge(int(studnum)-1))
        grants = q.getfirst("grants", group.getGrants(int(studnum)-1))
        address = q.getfirst("address", group.getAddress(int(studnum)-1))
        if group.checkClass(int(studnum)-1) == "Monitor":
            phone = q.getfirst("phone", group.getPhone(int(studnum)-1))
            email = q.getfirst("email", group.getEmail(int(studnum)-1))
        
        if studnum is not None:
            print ("""<form action=""" + '"' + selfurl + '"' + """>
                <input value =""" + '"' + q['student'].value + '"' + """type="text" name="student" style="display: none;">
                <input value = 2 type="text" name="choice" style="display: none;">
                <input value = """ + '"' + studnum + '"' + """ type="text" name="num" style="display: none;">
                <input placeholder="ФИО" value = """ + '"' + name + '"' + """ type="text" name="name">
                <input placeholder="Возраст" value = """ + '"' + age + '"' + """ type="text" name="age">
                <input placeholder="Стипендия" value = """ + '"' + grants + '"' + """ type="text" name="grants">
                <input placeholder="Адрес" value = """ + '"' + address + '"' + """ type="text" name="address">""")
            if group.checkClass(int(studnum)-1) == "Monitor":
                print("""<input placeholder="Телефон" value = """ + '"' + phone + '"' + """ type="text" name="phone">
                    <input placeholder="Эл. почта" value = """ + '"' + email + '"' + """ type="text" name="email">""")
                student = Monitor(None,None,None,None,None,None).getForm(q)
            else:
                student = Student(None,None,None,None).getForm(q)
            print("""<input value='Редактировать' type="submit">
            </form>""")            
            if student.getName() is not None:
                exec_edit(studnum,group, q, selfurl, student)   
    return