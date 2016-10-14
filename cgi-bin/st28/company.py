from .programmer import *
import pickle

class Company():
	_fileName = 'cgi-bin/st28/data.pkl'

	def __init__(self):
		self._employees = []

	def add(self, selfurl, q):
		self.printCompany(selfurl, q)
			
	def edit(self, selfurl, q):
		edit = True
		if 'typeEmployee' in q:
			typeEmployee = q['typeEmployee'].value

			if q['num'].value == 'last':
				num = len(self._employees)
			else:
				num = int(q['num'].value)
				self._employees.pop(num)

			name = q['name'].value if 'name' in q else ''
			age = q['age'].value if 'age' in q else ''
			salary = q['salary'].value if 'salary' in q else ''
			programmingLanguages = q['programmingLanguages'].value if 'programmingLanguages' in q else ''

			if typeEmployee == 'Employee':
				self._employees.insert(num, Employee(name, age, salary))
			else:
				self._employees.insert(num, Programmer(name, age, salary, programmingLanguages))

			self.save()
			edit = False
	
		self.printCompany(selfurl, q, edit)

	def delete(self, selfurl, q):
		self._employees.pop(int(q['num'].value))
		self.save()
		self.printCompany(selfurl, q)

	def clear(self):
		self._employees = []

	def printCompany(self, selfurl, q, edit = False):
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

		if 'select' in q and q['select'].value == '0':
			print ("""<tr">
				<td> <select name='typeEmployee'> <option value='Employee'> Работник </option> <option value='Programmer'> Программист </option> </select> </td>
				<td> <input type='text' name='name'> </td>
				<td> <input type='text' name='age'> </td>
				<td> <input type='text' name='salary'> </td>
				<td> <input type='text' name='programmingLanguages'> </td>
				<td colspan=2> <input value='Сохранить' type='submit'> </td>
    			<input value = {0} type="text" name="student" style="display: none;">
    			<input value = '1' type="text" name="select" style="display: none;">
    			<input value = 'last' type="text" name="num" style="display: none;">
				</tr>""".format(q['student'].value)
			)
			
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