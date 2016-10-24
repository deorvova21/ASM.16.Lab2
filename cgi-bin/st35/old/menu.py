
from .userlist import *


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
