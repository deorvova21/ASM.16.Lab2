from .student import *
from .monitor import *
import cgi

def exec_add(typeadd,group, q, selfurl):
    try:
        add_actions[typeadd](group, q, selfurl)
    except KeyError:
        print("Invalid selection!\n")
        add_actions['add'](group, q, selfurl)           
    return

def add(group, q, selfurl):
    typeadd = q.getfirst("typeadd", None)
    if typeadd != str(1) and typeadd != str(2):
        print ('<br><a href="{0}?student={1}&choice=1&typeadd=1">Добавить студента</a> | <a href="{0}?student={1}&choice=1&typeadd=2">Добавить старосту</a>'.format(selfurl, q['student'].value))
    if typeadd is not None:
        exec_add(typeadd,group, q, selfurl)    
    return

def student(group, q, selfurl):
    print ("""<form action=""" + '"' + selfurl + '"' + """>
        <input value =""" + '"' + q['student'].value + '"' + """type="text" name="student" style="display: none;">
        <input value = 1 type="text" name="choice" style="display: none;">
        <input value = 1 type="text" name="typeadd" style="display: none;">
        <input placeholder="ФИО" type="text" name="name">
        <input placeholder="Возраст" type="text" name="age">
        <input placeholder="Стипендия" type="text" name="grants">
        <input placeholder="Адрес" type="text" name="address">
        <input value='Добавить' type="submit">
    </form>""")
    name = q.getfirst("name", None)
    if name is not None:
        age = q.getfirst("age", None)
        grants = q.getfirst("grants", None)
        address = q.getfirst("address", None)
        student = Student(name, age, grants, address)
        group.load()
        group.add(student)
        group.save()
        print ('<br><a href="{0}?student={1}">Назад</a>'.format(selfurl, q['student'].value))
    return

def monitor(group, q, selfurl):
    print ("""<form action=""" + '"' + selfurl + '"' + """>
        <input value =""" + '"' + q['student'].value + '"' + """type="text" name="student" style="display: none;">
        <input value = 1 type="text" name="choice" style="display: none;">
        <input value = 2 type="text" name="typeadd" style="display: none;">
        <input placeholder="ФИО" type="text" name="name">
        <input placeholder="Возраст" type="text" name="age">
        <input placeholder="Стипендия" type="text" name="grants">
        <input placeholder="Адрес" type="text" name="address">
        <input placeholder="Телефон" type="text" name="phone">
        <input placeholder="Эл. почта" type="text" name="email">
        <input value='Добавить' type="submit">
    </form>""")
    name = q.getfirst("name", None)
    if name is not None:
        age = q.getfirst("age", None)
        grants = q.getfirst("grants", None)
        address = q.getfirst("address", None)
        phone = q.getfirst("phone", None)
        email = q.getfirst("email", None)
        student = Monitor(name, age, grants, address, phone, email)
        group.load()
        group.add(student)
        group.save()
        print ('<br><a href="{0}?student={1}">Назад</a>'.format(selfurl, q['student'].value))
    return

add_actions = {
    'add': add,
    '1': student,
    '2': monitor
}