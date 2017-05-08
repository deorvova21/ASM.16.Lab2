import pickle, copy, os
from .game_aaa import Game_AAA
from .game_mobile import Game_Mobile

class Function:
    def __init__(self, q, selfurl):
        self.l=list()
        self.q = q
        self.selfurl = selfurl

    def f(self):
        print(self.selfurl)
        print('<a href="{0}?student={1}&lol={2}">{3}</a>'.format(self.selfurl, self.q['student'].value, 3, "fds"))
        print(self.q)

    def read(self):
        self.read_file()
        if ('type' in self.q):       
            if (self.q['type'].value!="3"):
                if (self.q['type'].value=="1"): Game_AAA(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="2"): Game_Mobile(self.q, self.selfurl).write_ch()
                if (self.q['type'].value=="4"): self.l[int(self.q['id'].value)].write_ch()
                print('<br><br><input type="submit" value="Save">')
                print('</form>')
            else:
                if (len(self.l)==int(self.q['id'].value)):
                    if (self.q['add'].value=="1"): self.l.append(Game_AAA(self.q, self.selfurl))
                    if (self.q['add'].value=="2"): self.l.append(Game_Mobile(self.q, self.selfurl))
                self.l[int(self.q['id'].value)].read()
                self.write_file()
                self.write()
        else:
            k=len(self.l)
            print('<a href="{0}?student={1}&action=1&type=1&id={2}">Game_AAA</a> | <a href="{0}?student={1}&action=1&type=2&id={2}">Game_Mobile</a>'.format(self.selfurl, self.q['student'].value, k))

    def write(self):
        self.read_file()
        if (len(self.l)!=0):
            print('<table border><Caption><H3>Game catalog</H3></Caption><tr><td>Game name</td><td>developer</td><td>Publisher</td><td>ReleaseDate</td><td>Genre</td><td>Price</td><td>Display</td><td>Action</td></tr>')
            i=0
            for o in self.l:
                print('<tr height="20">')
                o.write()
                if type(o) is Game_AAA: print('<td>Not included</td>')
                print('<td><a href="{0}?student={1}&action=1&type=4&id={2}">Edit</a> | <a href="{0}?student={1}&action=3&id={2}">Delete</a></td>'.format(self.selfurl, self.q['student'].value,i))
                print('</tr>')
                i+=1
            print('</table>')
        print('<br><br><a href="{0}">Back</a> | <a href="{0}?student={1}&action=1">Add Games</a>'.format(self.selfurl, self.q['student'].value))

    def delete(self):
        self.read_file()
        self.l.pop(int(self.q['id'].value))
        self.write_file()
        self.write()       
            
       
    def read_file(self):
        if (os.path.exists("cgi-bin/st15/file.dat")):
            self.l = pickle.load(open("cgi-bin/st15/file.dat", "rb"))

    def write_file(self):
        pickle.dump(self.l, open("cgi-bin/st15/file.dat", "wb"))
