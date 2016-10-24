import glob
import os
import pickle
import re

from functools import reduce

from .user import *

class USERLIST():
    __slots__=('table')

    def __init__(self,user=None):
        self.table = []

    def append(self):
        self.table.append((USER()()))

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
        return (str(glob.glob('./cgi-bin/st35/**.pkl')))
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
        path=os.path.normpath("./cgi-bin/st35/"+str(file+'.pkl'))
        print(path)
        if os.path.exists(path):
            with open(path,'rb')as myfile:          #TODO st35/
                print("load OK\n")
                self.table=pickle.load(myfile)
        else:print("FileNotFoundError")


    def save(self):
        path=os.path.normpath("./cgi-bin/st35/"+str(input('save as: ')+'.pkl'))
        with open(path,'wb')as myfile:          #TODO st35/
            pickle.dump(self.table,myfile)
            print ("save OK")


    def edit(self,userlist,index):
        newuser = USER(list=userlist.table[int(index)])
        newuser.edit()
        userlist.table[int(index)] = newuser()
        userlist.save()


    def __delitem__(self,index):
        if 0<=int(index)<=int(self.table.__len__())-1:
            self.table.pop(int(index))
            print('del OK.')
            self.save()
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

