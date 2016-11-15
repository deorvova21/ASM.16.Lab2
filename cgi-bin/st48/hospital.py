import pickle, os, cgi
from .diagnosis import *

class Hospital:
	def __init__(self, q, selfurl):
		self.patients=[]
		self.q = q
		self.selfurl = selfurl
		self.load()
	
	def add_patient(self):
		patient = Patient()
		#patient.output_data()
		self.patients.append(patient)
		self.save()
		self.edit()

	def add_diagnosis(self):
		diagnosis = Diagnosis()
		#diagnosis.output_data()
		self.patients.append(diagnosis)
		self.save()
		self.edit()
		
	def display(self):
		print("""<form><table border="1" bgcolor="#c0c0c0" bordercolor="#800000"><tr align="center"><td>Имя пациента</td><td>Возраст</td><td>Диагноз</td><td>Лечащий врач</td><td>Способ лечения</td><td>Настройки</td></tr> """) 
		i = 0
		for item in self.patients:
			print('<tr>')
			item.all_data()
			print('<td><a href={0}?student={1}&act=edit&id={2}>Редактировать</a><br><a href={0}?student={1}&act=delete&id={2}>Удалить</a></td></tr></tr>'.format(self.selfurl, self.q.getvalue('student'), i))
			i+=1
		print("""</table><br><input type="hidden" name="student" value={0} />
<input type="hidden" name="act" value="display" />
<input type="hidden" name="id" id="id" value="0" />
<br><a href={0}?student={1}&act=add_patient>Добавить пациента</a><tr>
<p><a href={0}?student={1}&act=add_diagnosis>Назначить лечение</a>
<p><a href={0}?student={1}&act=clear>Очистить список</a>
<p><a href={0}>Выход</a>
</form>""".format(self.selfurl, self.q.getvalue('student')))

	def print_list(self):
		self.patients[int(self.q.getvalue('id'))].input_data(self.q)
		self.save()
		self.display()
	
	def edit(self):
		print("""<form>  
<input type="hidden" name="student" value="{0}" />
<input type="hidden" name="act" value="print_list" />""".format(self.q.getvalue('student')))
		sid = str()
		if 'id' in self.q:
			sid = self.q.getvalue('id')
		else:
			sid = str(len(self.patients)-1)
		print('<input type="hidden" name="id" value="{0}" />'.format(sid))
		print('<table>')
		self.patients[int(sid)].output_data()
		print('</table>')
		print('<p><input type="submit" value="Сохранить">')
		print('</form>')
		
	def save(self):
		pickle.dump(self.patients, open('cgi-bin/st48/list.bin', 'wb'))

	def load(self):
		if (os.path.exists('cgi-bin/st48/list.bin')):
			self.patients = pickle.load(open('cgi-bin/st48/list.bin', 'rb'))

	def delete(self):
		self.patients.pop(int(self.q.getvalue('id')))
		self.save()
		self.display()

	def clear(self):
		self.patients.clear()
		self.save()
		self.display()