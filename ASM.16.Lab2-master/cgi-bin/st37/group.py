from .feline import *
from .cat import *
import pickle
import cgi

class Group:
    __container=[]

    def __init__(self, q, selfurl, data=[]):
        self.__container=data
        self.q=q
        self.selfurl=selfurl

    def fadd(self, elem):   
        self.__container.append(elem)

    def add(self, q, selfurl):
        action = q.getfirst('action', None)
        if action is not None and action == 'add':
            ttype = q.getfirst('ttype', None)
            if ttype == '1' or ttype == '0':
                self.add_func(q, selfurl, ttype)
            else:
                print ("""<h3>
                <a href="{0}?student={1}&action=add&ttype=0">Add a feline</a> |
                <a href="{0}?student={1}&action=add&ttype=1">Add a cat</a>
                </h3>""".format(selfurl, q['student'].value))         
        else:
            print("<h3>Invalid type!</h3>")
            print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))

    def add_func(self, q, selfurl, ttype):
        elem = None
        formString = """<form action=""" + '"' + selfurl + '"' + ">" + """
        <input value =""" + '"' + q['student'].value + '"' + """type="text" name="student" style="display: none;">
        <input value = add type="text" name="action" style="display: none;">
        <input value = {} type="text" name="ttype" style="display: none;">
        <input placeholder="input kind" type="text" name="Kind">
        <input placeholder="input age" type="text" name="Age">
        <input placeholder="input weight" type="text" name="Weight">""".format(ttype)
        if ttype == '0':
            elem = Feline()
            formString += """<input value="Add the feline" type="submit">"""
        else:
            elem = Cat()
            formString += """ <input placeholder="input name" type="text" name="Name">
        <input placeholder="input owner's name" type="text" name="Owner">
        <input value="Add the cat" type="submit">"""
            
        formString += """ </form>"""
        print(formString)
        print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))
        elem.getFromForm(q)
        if elem.getKind() is not None:
            self.fadd(elem)
            self.fwrite()
            print(""" <h3>Completed!</h3>""")
        
    def fedit(self,index,elem):
        self.__container[index] = elem

    def edit(self, q, selfurl):
        if self.flen() == 0:
            print("<h3> The list is empty!<br>Please, add any 'felines'!</h3>")
        else:
            index = q.getfirst('index', None)
            elem = None
            try:
                elem = self.getElement(int(index))
                formString = """<form action=""" + '"' + selfurl + '"' + """>
                <input value =""" + '"' + q['student'].value + '"' + """type="text" name="student" style="display: none;">
                <input value = edit type="text" name="action" style="display: none;">
                <input value = """ + '"' + index + '"' + """ type="text" name="index" style="display: none;">
                {}
                <input value='Edit' type="submit">
            </form>""".format(elem.getInputs(q))
                print(formString)
                elem.getFromForm(q)
                print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))
                if elem.getKind() is not None:
                    self.fedit(int(index), elem)
                    self.fwrite()
                    print(""" <h3>Completed!</h3>""")
            except (ValueError, IndexError):
                print("""<h3>Invalid index!</h3>""")       
                print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))
    
    def fdel(self, q, selfurl):
        if self.flen() == 0:
            print("<h3> The list is empty!<br>Please, add any 'felines'!</h3>")
            print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))
        else:
            index = q.getfirst('index', None)
            if index is not None:
                try:
                    self.__container.pop(int(index))
                    self.fwrite()
                    print(selfurl)
                    self.fshow(q, selfurl)
                except (ValueError, IndexError):
                    print("<h3>Invalid index!</h3>")
                    print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))

    def fshow(self, q, selfurl):
        if self.flen()>0:
            titleString = """<h1>The Cat Family</h1>
        <h3>
        <a id="back" href="{0}"><-Back</a>
        <a href="{0}?student={1}&action=add">Add new feline or cat</a>
        </h3>""".format(selfurl, q['student'].value)
            tableString = """ {}<table>
                        <tr>
                            <th>Kind</th>
                            <th>Age</th>
                            <th>Weight</th>
                            <th>Name</th>
                            <th>Owner</th>
                        </tr> """.format(titleString)
            
            for ind in range(self.flen()):
                tableString += """<tr>""" + self.getElement(ind).print_object() + """
                <td class="tools"><a href={0}?student={1}&action=edit&index={2}>Edit</a></td>
                <td class="tools"><a href={0}?student={1}&action=del&index={2}>Delete</a></td>
                </tr>""".format(selfurl, q['student'].value, ind)
            print(tableString)
        else:
            print('<h3> The list is empty!<br>Please, add any felines!</h3>')
            print(""" <h3 id="back"><a href="{0}?student={1}"><-Back</a></h3>""".format(selfurl, q['student'].value))

    def fclear(self):
        self.__container.clear()

    def fread(self):
        with open("cgi-bin/st37/data.dat","rb") as file:
            self.__container = pickle.load(file)

        
    def fwrite(self):
        with open("cgi-bin/st37/data.dat","wb") as file:
            pickle.dump(self.__container,file)
            
    def flen(self):
        return len(self.__container)
    
    def getElement(self, index):
        return self.__container[index]
