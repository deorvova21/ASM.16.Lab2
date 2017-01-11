import pickle, cgi, os
from .contract import *

class List:
    def __init__(self, q, selfurl):
        self.agents = []
        self.q = q
        self.selfurl = selfurl

    def AddFree(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addfree" />')
        print('<table>')
        Free().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def AddContract(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        print('<input type="hidden" name="id" value="addcontract" />')
        print('<table>')
        Contract().ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def ShowList(self):
        i = 0
        for item in self.agents:
            print('<br>')
            item.Write()
            print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
            print('<br>')
            i+=1
        print('<br>')
        print('<a href={0}?student={1}&act=addfree>Добавить свободного агента</a> '.format(self.selfurl, self.q.getvalue('student')))
        print('<a href={0}?student={1}&act=addcontract>Добавить контракт</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}?student={1}&act=clear>Очистить список</a>'.format(self.selfurl, self.q.getvalue('student')))
        print('<p><a href={0}>Назад</a>'.format(self.selfurl))

    def Get(self):
        if self.q.getvalue('id') == 'addfree':
            agent = Free()
            agent.SaveEdit(self.q)
            self.agents.append(agent)
        elif self.q.getvalue('id') == 'addcontract':
            agent = Contract()
            agent.SaveEdit(self.q)
            self.agents.append(agent)
        else:
            self.agents[int(self.q.getvalue('id'))].SaveEdit(self.q)
        self.ShowList()

    def Edit(self):
        print('<form>')
        print('<input type="hidden" name="student" value="{0}" />'.format(self.q.getvalue('student')))
        print('<input type="hidden" name="act" value="get" />')
        iid = self.q.getvalue('id')
        print('<input type="hidden" name="id" value="{0}" />'.format(iid))
        print('<table>')
        self.agents[int(iid)].ShowEdit()
        print('</table>')
        print('<input type="submit" value="Сохранить">')
        print('</form>')

    def Save(self):
        pickle.dump(self.agents, open('cgi-bin/st30/agents.bin', 'wb'))

    def Load(self):
        if (os.path.exists('cgi-bin/st30/agents.bin')):
            self.agents = pickle.load(open('cgi-bin/st30/agents.bin', 'rb'))

    def Delete(self):
        self.agents.pop(int(self.q.getvalue('id')))
        self.ShowList()

    def Clear(self):
        self.agents.clear()
        self.ShowList()
