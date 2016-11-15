import cgi
from .patient import *

class Diagnosis(Patient):
		
		def __init__(self):
			super().__init__()
			self.Treatment=''
		
		def all_data(self):
			print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.Name, self.Age, self.Diagnosis, self.Doctor, self.Treatment))
		
		def input_data(self, q):
			super().input_data(q)
			self.Treatment = q.getvalue('Treatment')
		
		def output_data(self):
			super().output_data()
			print("""<tr><td>Способ лечения:</td><td><input type="text" name="Treatment" value="{}"></td></tr> </table>""".format(self.Treatment))