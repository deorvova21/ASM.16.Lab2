import datetime
import hashlib
import glob
import os
import pickle
import sqlite3

class USER():
    __slots__= ('user_info')

    def __init__(self,info=False,list=False):
        if not list:self.user_info={'surname':info['surname'].value,
                                    'name':info['name'].value,
                                    'username':info['username'].value,
                                    'hash':hashlib.sha512(str(info['password'].value).encode("UTF8")).hexdigest(),
                                    'date':str(datetime.datetime.now())}
        else:self.user_info=list

    def __call__(self):
        return self.user_info

    def __getattr__(self, item):
        return ("NoAttr")

    def edit(self,info):
        self.user_info['username'] = info['edit_Username'].value
        self.user_info['hash'] = hashlib.sha512(str(info['edit_Password'].value).encode("UTF8")).hexdigest()
        self.user_info['date_edit']=str(datetime.datetime.now())
        self.user_info['surname']=info['edit_Surname'].value
        self.user_info['name']=info['edit_Name'].value                                               #TODO


class USERLIST():
    __slots__=('table')

    def __init__(self,user=None):
        self.table = []

    def append(self,info):
        self.table.append((USER(info)()))

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
        if os.path.exists(path):
            with open(path,'rb')as myfile:
                self.table=pickle.load(myfile)

    def save(self,file):
        path=os.path.normpath("./cgi-bin/st35/data/"+str(file)+'.pkl')
        with open(path,'wb')as myfile:
            pickle.dump(self.table,myfile)

    def edit(self,info):
        newuser = USER(list=self.table[int(info['index'].value)])
        newuser.edit(info)
        self.table[int(info['index'].value)] = newuser()
        self.save(info['userlist'].value)

    def __delitem__(self,index):
        if 0<=int(index)<=int(self.table.__len__())-1:
            self.table.pop(int(index))
        else:
            print("no index")


class DataBase():

    __slots__ = ('connect',
                 'cc',
                 'queries')

    def __init__(self):
        self.queries = {
            'SELECT': 'select {SELECT} from {FROM} where {WHERE}',
            #'SELECT_ALL': 'select {} from {}',#'INSERT': 'insert into {} values({})',#'UPDATE': 'update {} set {} where {}',#'DELETE': 'delete from {} where {}',
            #'DELETE_ALL': 'delete from {}',#'CREATE_TABLE': 'create table if not exists {}({})',#'DROP_TABLE': 'drop table {}',#'CHECK_TABLE': 'select name from sqlite_master where type=\'table\' order by name'
        }
        self.connect= sqlite3.connect(database=os.path.normpath('./cgi-bin/st35/data/test.sqlite3'))
        self.cc=self.connect.cursor()

    def __call__(self,queries,**arg):
        query = self.queries[queries].format(**arg)
        ret=()
        for row  in self.cc.execute(query):ret+=row
        return ret

