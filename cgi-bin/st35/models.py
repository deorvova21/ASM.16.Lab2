import datetime
import hashlib
import glob
import os
import pickle

class DataUser (object):
    __slots__ = ('surname', 'name', 'group')

    def __init__(self,form_surname,form_name):
        self.surname=form_surname
        self.name=form_name
        #self.group = group TODO

    def __str__(self):
        print("surname: {}\nname: {}\n".
              format(
            self.surname,
            self.name
        ))
        return("")

class USER(DataUser):
    __slots__= ('id',
                'username',
                'hash',
                'date',
                'create',
                'date_edit',
                'qwerty')

    def __init__(self,form_username=False,form_password=False,form_surname=False,form_name=False,list=False):
        if not list:
            DataUser.__init__(self,form_surname,form_name)                                            #TODO
            username = form_username
            password = form_password
            try:
                if ((username.__len__()>=1)and(password.__len__()>=1)):        #TODO
                    self.id,self.username,self.hash,self.date,self.create,self.date_edit=\
                    0,\
                    username,\
                    hashlib.sha512(str(password).encode("UTF8")).hexdigest(),\
                    str(datetime.datetime.now()),\
                    True,\
                    False
                else:
                    self.create = False
                    #print("create=False:error_len")
            except AttributeError:
                self.create = False
                #print("create=False:error_atribute")                           #TODO
            else:
                if (self.create == True):
                    pass
                    #print("create=True\n")
        else:
            self.id,self.username,self.hash,self.date,self.date_edit,self.create,self.surname,self.name= \
                list.get("id"), \
                list.get("username"), \
                list.get("hash"), \
                list.get("date"), \
                list.get("date_edit"), \
                True,\
                list.get("surname"), \
                list.get("name")

    def __str__(self):
        return ''.join("id:{}<br>username:{}<br>hash:{}<br>date:{}<br>date_edit:{}<br>surname:{}<br>name:{}<br>".
                format(self.id,
                       self.username,
                       self.hash,
                       self.date,
                       self.date_edit,
                       self.surname,
                       self.name
                       )
                )

    def __call__(self):
        return {
            "id":self.id,
            "username":self.username,
            "hash":self.hash,
            "date":self.date,
            "date_edit":self.date_edit,
            "surname":self.surname,
            "name":self.name
                }

    def __getattr__(self, item):
        return ("NoAttr")

    def __bool__(self):
        return self.create

    def edit(self,username,password,surname,name):
        self.username = username
        self.hash = hashlib.sha512(str(password).encode("UTF8")).hexdigest()
        self.date_edit=str(datetime.datetime.now())
        DataUser.__init__(self,surname,name)                                                #TODO

class USERLIST():
    __slots__=('table')

    def __init__(self,user=None):
        self.table = []

    def append(self,form_username,form_password,form_surname,form_name):
        self.table.append((USER(form_username,form_password,form_surname,form_name)()))

    def __str__(self):
        if self.table == []:
            return("список не найден")
        else:
            for index in range(self.table.__len__()):
                newuser=USER(list=self.table[index])
                print("index: ",index,"<br><br>",newuser)
            return("")

    def view_all_userlist():
        #lr = [(r'\[|\]|\'|\ |\./st35/|.pkl|\./st35\\|\\|\./cgi-bin/st35',''),(r',', '\n'),]
        return (glob.glob('./cgi-bin/st35/data/**.pkl'))
        #return ( "Userlist:<br>"+reduce(lambda v, it: re.sub(it[0], it[1], v), lr, str(glob.glob('./cgi-bin/st35/**.pkl')))+"<br><br>")

    def delite_user_list():
        try:
            os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)),str(input('file name: ', )) + '.pkl'))
        except FileNotFoundError:
            print("FileNotFoundError")
        else:
            print("del OK")
        return

    def load(self,file):
        path=os.path.normpath("./cgi-bin/st35/data/"+str(file+'.pkl'))
        #print(path)
        if os.path.exists(path):
            with open(path,'rb')as myfile:          #TODO st35/
                #print("load OK\n")
                self.table=pickle.load(myfile)
        #else:print("FileNotFoundError")


    def save(self,file):
        path=os.path.normpath("./cgi-bin/st35/data/"+str(file)+'.pkl')
        with open(path,'wb')as myfile:          #TODO st35/
            pickle.dump(self.table,myfile)



    def edit(self,userlist,index,username,password,surname,name):

        newuser = USER(list=self.table[int(index)])

        newuser.edit(username=username,password=password,surname=surname,name=name)

        self.table[int(index)] = newuser()

        self.save(userlist)


    def __delitem__(self,index):
        if 0<=int(index)<=int(self.table.__len__())-1:
            self.table.pop(int(index))
            #self.save()
        else:
            print("no index")




        # def __getattr__(self, item):
        # pass

         # def __call__(self, *args, **kwargs):
        # print ("call")

        # def __len__(self):
        # return len(self.table)

        # def __getitem__(self, item):
        # pass

        # def __setitem__(self, key, value):
        # pass

class MENU():
    "MENU:\n"

    def __init__(self):
        self.menu_userlist = {str(self.open_userlist.__doc__).split('.')[0]:self.open_userlist,
                              str(self.viev_all_userlist.__doc__).split('.')[0]:self.viev_all_userlist,
                              str(self.create_userlist.__doc__).split('.')[0]:self.create_userlist,
                              str(self.delite_userlist.__doc__).split('.')[0]:self.delite_userlist,
                              str(self.edit_list.__doc__).split('.')[0]: self.edit_list,
                              str(self.add_user.__doc__).split('.')[0]: self.add_user,
                              str(self.del_user.__doc__).split('.')[0]: self.del_user
                              }

    def __str__(self):

        print(MENU.__doc__)
        for i in self.menu_userlist.values():
            print(i.__doc__)
        return ("")

    def __call__(self,flag):
        return  self.menu_userlist.get(flag)()

    def open_userlist(self):
        "1. Open userlist"
        list = USERLIST()
        list.load()
        print(list)

    def viev_all_userlist(self):
        "2. View all userlist"
        print (USERLIST.view_all_userlist())

    def create_userlist(self,flag='Y'):
        "3. Create userlist"

        list = USERLIST()

        while flag == 'Y':
            list.append()
            flag = input("Add new user? (Y/N): ", )

        list.save()

    def delite_userlist(self):
        "4. Delite user list"
        USERLIST.delite_user_list()

    def edit_list(self):
        "5. Edit_list"
        list = USERLIST()
        list.load()
        list.edit(list,input("index: ",))

    def add_user(self,flag='Y'):
        "6. Add_user"
        list = USERLIST()
        list.load()
        while flag=='Y':
            list.append()
            flag = input("Add new user? (Y/N): ", )
        list.save()

    def del_user(self):
        "7. Del user"
        list = USERLIST()
        list.load()
        del list[input('index: ')]