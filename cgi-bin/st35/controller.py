from .view import view
from .models import USERLIST

class Controller:

    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl=selfurl

    def index(self):
        View = view(self.q, self.selfurl)
        base = View.base()
        dropdown_menu = View.dropdown_menu()
        print(base.format(left_container=dropdown_menu, right_container=""))

    def userlist(self):
        View = view(self.q, self.selfurl)
        base = View.base()
        dropdown_menu = View.dropdown_menu()
        print(base.format(left_container=dropdown_menu, right_container=View.gen_table(self.q['userlist'].value)))

    def del_user(self):
        userlist = USERLIST()
        userlist.load(self.q['userlist'].value)
        del userlist[self.q['del_item'].value]
        userlist.save(self.q['userlist'].value)

    def main(self):

        if 'del_item' in self.q and 'userlist' in self.q:
            self.del_user()
            self.userlist()

        if self.q.__len__() == 1:
            self.index()
        else:

            if 'Username' in self.q and 'Password' in self.q and 'Surname' in self.q and 'Name' in self.q:
                userlist = USERLIST()
                userlist.load(self.q['userlist'].value)
                userlist.append(self.q['Username'].value,self.q['Password'].value,self.q['Surname'].value,self.q['Name'].value)
                userlist.save(self.q['userlist'].value)
                self.userlist()

            if  'edit_Username' in self.q and \
                'edit_Password' in self.q and \
                'edit_Surname' in self.q and \
                'edit_Name' in self.q and \
                'index' in self.q and \
                'userlist' in self.q:
                userlist = USERLIST()
                userlist.load(self.q['userlist'].value)
                userlist.edit(userlist=self.q['userlist'].value,
                              index=self.q['index'].value,
                              username=self.q['edit_Username'].value,
                              password=self.q['edit_Password'].value,
                              surname=self.q['edit_Surname'].value,
                              name=self.q['edit_Name'].value,
                              )
                self.userlist()

            if 'userlist' in self.q and self.q.__len__() == 2:
                    self.userlist()







