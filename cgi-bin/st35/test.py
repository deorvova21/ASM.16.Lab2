
import cgi
#from .controller import Controller

form = cgi.FieldStorage()

Userlist = form.getfirst("Userlist", "не задано")
Username = form.getfirst("Username", "не задано")
Password = form.getfirst("Password", "не задано")
Surname = form.getfirst("Surname", "не задано")
Name= form.getfirst("Name", "не задано")

#userlist = USERLIST()
#userlist.load(Userlist)
#userlist.append(form_username,form_password,form_surname,form_name)

print("Content-type: text/html; charset=utf-8\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Userlist: {}</p>".format(Userlist))
print("<p>Username: {}</p>".format(Username))
print("<p>Password: {}</p>".format(Password))
print("<p>Surname: {}</p>".format(Surname))
print("<p>Name: {}</p>".format(Name))
print("""</body>
        </html>""")


