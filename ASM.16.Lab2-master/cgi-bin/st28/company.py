from .programmer import *
import pickle

class Company():
	_fileName = 'cgi-bin/st28/data.pkl'

	def __init__(self):
		self._employees = []

	def add(self, typeEmployee, name, age, salary, programmingLanguages):
		if typeEmployee == 'Employee':
			self._employees.append(Employee(name, age, salary))
		else:
			self._employees.append(Programmer(name, age, salary, programmingLanguages))

	def edit(self, typeEmployee, num, name, age, salary, programmingLanguages):
		self._employees.pop(num)
		if typeEmployee == 'Employee':
			self._employees.insert(num, Employee(name, age, salary))
		else:
			self._employees.insert(num, Programmer(name, age, salary, programmingLanguages))

	def delete(self, num):
		self._employees.pop(num)

	def clear(self):
		self._employees = []

	def printCompany(self, selfurl, q, edit):
		print ("<form action='" + selfurl +"""'>
			<table border=1 align='center' cellspacing='0' cellpadding='5' style="margin-top: 30px;"> <tr bgcolor='#90e4a3' style="font-size: 20px">
			<th> Класс					</th>
			<th> Имя					</th>
			<th> Возраст				</th>
			<th> Зарплата				</th>
			<th> Языки программирования	</th>
			<th> 						</th>
			<th>						</th> </tr>""")

		for i, employee in enumerate(self._employees):
			print (employee.printEmployee(selfurl, q, i, edit))
			
		print ("""<tr bgcolor='#e0ffe7' style="font-size: 18px">
			<td colspan=5> <a href='{0}'> Выйти </a> </td>
			<td colspan=2> <a href='{0}?student={1}&select=0'> Добавить </a> </td>
			</tr>""".format(selfurl, q['student'].value)
		)

	def save(self):
		file = open(self._fileName, 'wb')
		pickle.dump(self._employees, file)
		file.close()

	def load(self):
		file = open(self._fileName, 'rb')
		self._employees = pickle.load(file)
		file.close()