from .models import USERLIST
from .models import DataBase

class view(object):

    def __init__(self, q, selfurl):
        self.info = {
            'q':q,
            'selfurl':selfurl,
            'student':q['student'].value,
            'url':'{selfurl}?student={student}'.format(selfurl=selfurl,student=q['student'].value)}
        self.templates={
            'table':self.open('table'),
            'tableitem':self.open('table_item'),
            'user_info_form':self.open('user_info_form'),
            'add_btn':self.open('add_user'),
            'user_edit_form':self.open('user_edit_form'),
            'dropdown_menu' : self.open('dropdown_menu'),
            'dropdown_menu_item' : self.open('dropdown_menu_item')}

    def open(self,file):
        mybase = DataBase()
        return(mybase(queries='SELECT', SELECT='html', FROM='templates', WHERE='name="{file}"'.format(file=file))[0])

    def gen_table(self ,userlist_name):
        table = self.templates['table']
        tableitem = self.templates['tableitem']
        user_info_form = self.templates['user_info_form']
        add_btn = self.templates['add_btn']
        user_edit_form = self.templates['user_edit_form']
        data = USERLIST()
        data.load(userlist_name)
        amt_data = data.table.__len__()
        tablenew = ''
        for i in range(amt_data):
            #TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            info_tableitem={
                    'username':data.table[i].get("username"),
                    'hash':data.table[i].get("hash"),
                    'date':data.table[i].get("date"),
                    'date_edit':data.table[i].get("date_edit"),
                    'surname':data.table[i].get("surname"),
                    'name':data.table[i].get("name"),
                    'index' : str(i),
                    'del_item':i,
                    'userlist':self.info['q']['userlist'].value,
                    'modal_user_item':data.table[i].get("username"),
                    'user_data':data.table[i].get("username")}
            tablenew += tableitem.format(
                **info_tableitem,
                user_edit_form=user_edit_form.format(**self.info,**info_tableitem),
                user_info_form=user_info_form.format(**info_tableitem),
                href_del=("{url}&userlist={userlist}&del_item={del_item}".format(**self.info,**info_tableitem)))
        add_btn = add_btn.format(userlist=self.info['q']['userlist'].value,**self.info)
        return (table.format(panel_title=userlist_name,
                             table_item=tablenew,
                             add_btn = add_btn))

    def base(self):
        return self.open('base')

    def error(self):
        return self.open('404')

    def dropdown_menu(self):
        dropdown_menu = self.templates['dropdown_menu']
        dropdown_menu_item = self.templates['dropdown_menu_item']
        amt_userlist = USERLIST.view_all_userlist().__len__()
        menu = ''
        for i in range(amt_userlist):
            userlist=USERLIST.view_all_userlist()[i].replace('./cgi-bin/st35/data\\', '').replace('.pkl', '')
            menu += (dropdown_menu_item.
                        format(userlist=userlist,href = ('{url}&userlist={userlist}'.format(**self.info,userlist=userlist))))
        return dropdown_menu.format(menu=menu, amt_userlist=amt_userlist)