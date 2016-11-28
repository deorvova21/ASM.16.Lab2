import pickle, cgi, os
from .Foreign import *

class Music:
    def __init__(self, q, selfurl):
        self.albums = []
        self.q = q
        self.selfurl = selfurl

    def AddNative(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addnative" />')
        print('<table>')
        Native().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def AddForeign(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addforeign" />')
        print('<table>')
        Foreign().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def ShowList(self):
        i = 0
        for item in self.albums:
            print('<br>')
            item.Write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<br>')
            i+=1
        print('<br>')
        print('<a href={0}?student={1}&act=addnative>Добавить российского исполнителя</a> '.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=addforeign>Добавить зарубежного исполнителя</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}>Назад</a>'.format(self.selfurl))

    def Get(self):
        if self.q.getvalue('id') == 'addnative':
            album = Native()
            album.SaveEdit(self.q)
            self.albums.append(album)
        elif self.q.getvalue('id') == 'addforeign':
            album = Foreign()
            album.SaveEdit(self.q)
            self.albums.append(album)
        else:
            self.albums[int(self.q.getvalue('id'))].SaveEdit(self.q)
        self.ShowList()

    def Edit(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        iid = self.q.getvalue('id')
        print('<input type="hidden" name="id" value="{0}" />'.format(iid))
        print('<table>')
        self.albums[int(iid)].ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def Save(self):
        pickle.dump(self.albums, open('cgi-bin/st36/list.bin', 'wb'))

    def Load(self):
        if (os.path.exists('cgi-bin/st36/list.bin')):
            self.albums = pickle.load(open('cgi-bin/st36/list.bin', 'rb'))

    def Delete(self):
        self.albums.pop(int(self.q.getvalue('id')))
        self.ShowList()

    def Clear(self):
        self.albums.clear()
        self.ShowList()
