class Employee:
	def __init__(self, name, age, salary):
		self.setName(name)
		self.setAge(age)
		self.setSalary(salary)

	def setName(self, name):
		self._name = name

	def setAge(self, age):
		self._age = age

	def setSalary(self, salary):
		self._salary = salary

	def getName(self):
		return self._name

	def getAge(self):
		return self._age

	def getSalary(self):
		return self._salary

	def printEmployee(self, url, q, i, edit):
		if edit == True and 'num' in q and i == int(q['num'].value):
			return ("""<tr">
				<td> <select name='typeEmployee'> <option value='Employee'> Работник </option> <option value='Programmer'> Программист </option> </select> </td>
				<td> <input type='text' name='name' value={0}> </td>
				<td> <input type='text' name='age' value={1}> </td>
				<td> <input type='text' name='salary' value={2}> </td>
				<td> <input type='text' name='programmingLanguages' > </td>
				<td colspan=2> <input value='Сохранить' type='submit'> </td>
        		<input value = {3} type="text" name="student" style="display: none;">
        		<input value = {4} type="text" name="select" style="display: none;">
        		<input value = {5} type="text" name="num" style="display: none;">
				</tr>""".format(self.getName(), self.getAge(), self.getSalary(), q['student'].value, q['select'].value, q['num'].value)
			)
		else:
			return ("""	<tr>
				<td> Работник </td>
				<td> {0} </td>
				<td> {1} </td>
				<td> {2} </td>
				<td>     </td>
				<td> <a href='{3}?student={4}&select=1&num={5}'> Редактировать </a> </td>
				<td> <a href='{3}?student={4}&select=2&num={5}'> Удалить </a> </td>
			</tr>""".format(self.getName(), self.getAge(), self.getSalary(), url, q['student'].value, i)
			)