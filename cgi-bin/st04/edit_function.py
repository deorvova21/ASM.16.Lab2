import cgi
def exec_edit(studnum,group, q, selfurl, name, age ,grants ,address, phone, email):
    try:
        int(studnum)
        group.check(int(studnum)-1)
        if group.checkClass(int(studnum)-1) == "Monitor":
             group.edit(int(studnum)-1, name, age, grants, address, phone, email)
        else:
            group.edit(int(studnum)-1, name, age, grants, address, None, None)
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
        form = cgi.FieldStorage()
        studnum = form.getfirst("num", None)
        name = form.getfirst("name", group.getName(int(studnum)-1))
        age = form.getfirst("age", group.getAge(int(studnum)-1))
        grants = form.getfirst("grants", group.getGrants(int(studnum)-1))
        address = form.getfirst("address", group.getAddress(int(studnum)-1))
        if group.checkClass(int(studnum)-1) == "Monitor":
            phone = form.getfirst("phone", group.getPhone(int(studnum)-1))
            email = form.getfirst("email", group.getEmail(int(studnum)-1))
        
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
            print("""<input value='Редактировать' type="submit">
            </form>""")
            form = cgi.FieldStorage()
            name = form.getfirst("name", None)
            if name is not None:
                age = form.getfirst("age", None)
                grants = form.getfirst("grants", None)
                address = form.getfirst("address", None)
                phone = form.getfirst("phone", None)
                email = form.getfirst("email", None)
                exec_edit(studnum,group, q, selfurl, name, age ,grants ,address, phone, email)   
    return