
from .models import USERLIST

class view(object):
    def __init__(self, q, selfurl):
        self.q = q
        self.selfurl = selfurl

    def open(self,file):
        return (open("./cgi-bin/st35/templates/"+file+".html", 'r')).read()

    def gen_table(self ,userlist_name):


        table = self.open('table')
        tableitem = self.open('table_item')
        user_info_form = self.open('user_info_form')
        add_btn = self.open('add_user')
        user_edit_form = self.open('user_edit_form')

        data = USERLIST()

        data.load(userlist_name)

        amt_data = data.table.__len__()

        tablenew = ''

        for i in range(amt_data):
            tablenew += tableitem.format(
                user_edit_form=user_edit_form.format
                (
                    id=self.q['student'].value,
                    selfurl =self.selfurl,
                    index=str(i),
                    Name =data.table[i].get("name"),
                    Surname=data.table[i].get("surname"),
                    Username = data.table[i].get("username"),
                    userlist =self.q['userlist'].value
                )
                ,
                user_info_form=user_info_form.format
                    (
                    username=data.table[i].get("username"),
                    hash=data.table[i].get("hash"),
                    date=data.table[i].get("date"),
                    date_edit=data.table[i].get("date_edit"),
                    surname=data.table[i].get("surname"),
                    name=data.table[i].get("name")
                ),




                modal_user_item=data.table[i].get("username"),
                user_data=data.table[i].get("username"),
                username=data.table[i].get("username"),
                href_del=("{selfurl}?student={student}&userlist={userlist}&del_item={del_item}".format
                                (
                                selfurl=self.selfurl,
                                student=self.q['student'].value,
                                userlist=self.q['userlist'].value,
                                del_item=i
                            )
                            )
            )

        add_btn = add_btn.format(userlist=self.q['userlist'].value, selfurl=('{0}?student={1}&userlist=test'.format(self.selfurl,
                                                                                        self.q['student'].value,

                                                                                                     ))
                                 , id=self.q['student'].value
                                 )

        return (table.format(panel_title=userlist_name, table_item=tablenew,add_btn = add_btn
                             )
                )

    def base(self):

        base = self.open('base')
        return base

    def dropdown_menu(self):

        dropdown_menu = self.open('dropdown_menu')
        dropdown_menu_item = self.open('dropdown_menu_item')
        amt_userlist = USERLIST.view_all_userlist().__len__()
        menu = ''
        for i in range(amt_userlist):
            userlist=USERLIST.view_all_userlist()[i].replace('./cgi-bin/st35/data\\', '').replace('.pkl', '')
            menu += (dropdown_menu_item.
                     format(userlist=userlist,
                            href = ("{selfurl}?student={student}&userlist={userlist}".format
                                (
                                selfurl=self.selfurl,
                                student=self.q['student'].value,
                                userlist=userlist
                                )
                                    )
                            )
                     )
        dropdown_menu = dropdown_menu.format(menu=menu, amt_userlist=amt_userlist)
        return dropdown_menu

