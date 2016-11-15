import cgi

class Patient:
	def __init__(self):
		self.Name=''
		self.Age=''
		self.Diagnosis=''
		self.Doctor=''
		
	def all_data(self):
		print('<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>'.format(self.Name, self.Age, self.Diagnosis, self.Doctor, 'empty'))

	def output_data(self):
		print("""<form><table border="1" bgcolor="#c0c0c0" bordercolor="#800000"> 
<tr><td>Имя пациента:</td><td><input type="text" name="Name" value="{}"></td><tr> 
<tr><td>Возраст:</td><td><input type="text" name="Age" value="{}"></td></tr> 
<tr><td>Диагноз:</td><td><input type="text" name="Diagnosis" value="{}"></td></tr> 
<tr><td>Лечащий врач:</td><td><input type="text" name="Doctor" value="{}"></td></tr>""".format(self.Name, self.Age, self.Diagnosis, self.Doctor))
		
	def input_data(self, q):
		self.Name = q.getvalue('Name')
		self.Age = q.getvalue('Age')
		self.Diagnosis = q.getvalue('Diagnosis')
		self.Doctor = q.getvalue('Doctor')