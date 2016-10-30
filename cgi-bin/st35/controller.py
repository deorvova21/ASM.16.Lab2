from .view import view
from .models import USERLIST
from .log import log

class Controller:

    def __init__(self, q, selfurl):
        self.log=log()
        self.q = q
        self.selfurl=selfurl
        self.view=view(self.q, self.selfurl)
        self.log(q=self.q.value,selfurl=self.selfurl,this_def="__init__",this_class="Controller")

    def index(self):
        base = self.view.base()
        dropdown_menu = self.view.dropdown_menu()
        print(base.format(left_container=dropdown_menu, right_container=""))
        self.log(q=self.q, this_def="index", this_class="Controller")

    def userlist(self):
        base = self.view.base()
        dropdown_menu = self.view.dropdown_menu()
        print(base.format(left_container=dropdown_menu, right_container=self.view.gen_table(self.q['userlist'].value)))
        self.log(q=self.q, this_def="userlist", this_class="Controller")

    def del_user(self):
        userlist = USERLIST()
        userlist.load(self.q['userlist'].value)
        del userlist[self.q['del_item'].value]
        userlist.save(self.q['userlist'].value)
        self.log(q=self.q, this_def="del_user", this_class="Controller")

    def main(self):
        self.log(q=self.q, this_def="main", this_class="Controller")
        if 'del_item' in self.q and 'userlist' in self.q:
            self.log(q=self.q, this_def="main(del_item)", this_class="Controller")
            self.del_user()
            self.userlist()
        elif self.q.__len__() == 1:
            self.log(q=self.q, this_def="main(index)", this_class="Controller")
            self.index()
        elif 'username' in self.q and 'password' in self.q and 'surname' in self.q and 'name' in self.q:
            self.log(q=self.q, this_def="main(userlist)", this_class="Controller")
            userlist = USERLIST()
            userlist.load(self.q['userlist'].value)
            userlist.append(self.q)
            userlist.save(self.q['userlist'].value)
            self.userlist()
        elif  'url' in self.q and self.q['url'].value=='edit':# TODO ERROR
            self.log(q=self.q, this_def="main(edit)", this_class="Controller")
            userlist = USERLIST()
            userlist.load(self.q['userlist'].value)
            userlist.edit(self.q)
            self.userlist()
        elif 'userlist' in self.q and self.q.__len__() == 2:
                self.userlist()
        else:# TODO ERROR
            self.log(q=self.q, this_def="main(404)", this_class="Controller")
            print(self.view.error())