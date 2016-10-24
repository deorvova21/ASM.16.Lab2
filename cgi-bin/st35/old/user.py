#!/usr/bin/python3
import datetime
import hashlib

from .datauser import *


class USER(DataUser):
    __slots__= ('id',
                'username',
                'hash',
                'date',
                'create',
                'date_edit')

    def __init__(self,list=False):
        if not list:
            DataUser.__init__(self)                                            #TODO
            username = input("username: ", )
            password = input("password: ", )
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
                    print("create=False:error_len")
            except AttributeError:
                self.create = False
                print("create=False:error_atribute")                           #TODO
            else:
                if (self.create == True):
                    print("create=True\n")
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

    def edit(self):
        self.username = input("newusername: ",)
        self.hash = hashlib.sha512(str(input("newpassword: ", )).encode("UTF8")).hexdigest()
        self.date_edit=str(datetime.datetime.now())
        DataUser.__init__(self)                                                #TODO
