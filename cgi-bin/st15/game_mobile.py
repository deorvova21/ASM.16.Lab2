from .game_aaa import Game_AAA
import cgi

class Game_Mobile(Game_AAA):
    def __init__(self, q, selfurl):
        super().__init__(q, selfurl)
        self.display=""
        self.q=q
        self.selfurl=selfurl
    
    def read(self):
        Game_AAA.read(self)
        if ('display' in self.q):
            self.display = self.q['display'].value
        else: self.display = ""

    def write(self):
        Game_AAA.write(self)
        print('<td>{0}</td>'.format(self.display))
        

    def write_ch(self):
        Game_AAA.write_ch(self)
        print('<br>Display:<br><input type="display" name="display" value="{0}">'.format(self.display))
    	

    
    
