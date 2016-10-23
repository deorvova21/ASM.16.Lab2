import pickle, os, cgi
from .Emploee import *
from .Chief  import *
class group:
	def __init__(self, q, selfurl):
                self.list=[]
                self.q=q
                self.selfurl= selfurl

	def load(self):
                if (os.path.exists("cgi-bin/st19/staff.dat")):
                        self.list=pickle.load(open("cgi-bin/st19/staff.dat", "rb"))

	def save(self):
                pickle. dump(self.list,open("cgi-bin/st19/staff.dat", "wb"))

	def add_chief(self):
                self.load()
                chief=Chief(self.q)
                self.list.append(chief)
                chief.add()
                chief.save_form(self.q)
                self.save()   

	def fi(self):
		print("st00.group.f()<br>")

	def clear_list(self):
		self.load()
		self.list.clear()
		self.save()
		self.show_list()

	def edit(self):
		self.load()
		self.list[int(self.q['id'].value)].edit_obj(self.q)
		self.list[int(self.q['id'].value)].save_form(self.q)
		self.save()

	def delete_obj(self):
                self.load()
                self.list.pop(int(self.q['id'].value))
                self.save()
                self.show_list()

	def add_emploee(self):
                self.load()
                empl=Emploee(self.q)
                self.list.append(empl)
                empl.add()
                empl.save_form(self.q)

	def show_list(self):
                self.load()
                print ('<br><a href="{0}">Back</a> | <a href="{0}?student={1}">Try again</a><br>'.format(self.selfurl, self.q['student'].value));
                if len(self.list) == 0:
                    print("<br>Empty list<br>")
                else:
                    print("""<table border><Caption><H3>Staff list</H3></Caption>
                  <tr><th colspan="3">Emploee</th><th colspan="2">Detail(only for chief)</th><th rowspan="2">Action</th></tr> 
                  <tr><th>Name</th><th>Department</th><th>Phone</th>
                  <th>Last Name</th><th>Status</th></tr>""")
                    i=0
                    for item in self.list:
                            item.show_form()
                            print("""<td><a href="{0}?student={1}&action=delete_obj&id={2}">Delete</a> or
                                <a href="{0}?student={1}&action=edit&id={2}">Edit</a>
                                </td>""".format(self.selfurl, self.q['student'].value, i))
                            print("</tr>")
                            i += 1
                print("</table>")
                print("""<br><a href="{0}?student={1}&action=add_emploee">Add emploee</a>
                         <br><a href="{0}?student={1}&action=add_chief">Add Chief</a>
                         <br><a href="{0}?student={1}&action=clear_list">Clear list</a>
                 """.format(self.selfurl, self.q['student'].value))
