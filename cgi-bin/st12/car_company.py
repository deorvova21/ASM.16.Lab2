import pickle, cgi, os
from .Driver import *
class Car_company:
    def __init__(self, q, selfurl):
        self.company =[]
        self.q=q
        self.selfurl=selfurl

    def add_car_company(self):
        self.load()
        car = Car()
        self.company.append(car)
        self.save()
        self.edit()
        

    def add_driver_company(self):
        self.load()
        driver = Driver()
        self.company.append(driver)
        self.save()
        self.edit()
        

    def edit(self):
        self.load()
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        sid = str()
        if 'id' in self.q:
            sid = self.q.getvalue('id')
        else:
            sid = str(len(self.company)-1)
        print('<input type="hidden" name="id" value="{0}" />'.format(sid))
        print('<table>')
        self.company[int(sid)].show_car()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')
        

    def print_all(self):
        self.load()
        i = 0
        for item in self.company:
            print('<br>')
            item.write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Change</a><br><a href={0}?student={1}&act=delete&id={2}>Delete</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<br>')
            i+=1
        print('<input type="hidden" name="student" value={0} />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="display" />')
        print('<br>')
        
        print('<a href={0}?student={1}&act=add_car_company>Add car</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('///')
        print('<a href={0}?student={1}&act=add_driver_company>Add driver</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}>Back</a>'.format(self.selfurl))
        print('<p><a href={0}?student={1}&act=clear>Clear</a>'.format(self.selfurl, self.q.getvalue('student')))

    def get(self):
        self.load()
        self.company[int(self.q.getvalue('id'))].edit_car(self.q)
        self.save()
        self.print_all()


    def save(self):
        pickle.dump(self.company, open('cgi-bin/st12/list.bin', 'wb'))

    def load(self):
        if (os.path.exists('cgi-bin/st12/list.bin')):
            with open('cgi-bin/st12/list.bin', 'rb') as f:
                self.company = pickle.load(f)

    def delete(self):
        self.load()
        self.company.pop(int(self.q.getvalue('id')))
        self.save()
        self.print_all()

    def clear(self):
        self.load()
        self.company.clear()
        self.save()
        self.print_all()
