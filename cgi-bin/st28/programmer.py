from .employee import *
import re

class Programmer(Employee):
	def __init__(self, name, age, salary, programmingLanguages):
		self.setProgrammingLanguages(programmingLanguages)
		super().__init__(name, age, salary)

	def setSalary(self, salary):
		self._salary = int(salary)*len(self._programmingLanguages)

	def setProgrammingLanguages(self, programmingLanguages):
		self._programmingLanguages = re.split('[,;][\s]*', programmingLanguages)

	def getProgrammingLanguages(self):
		return ', '.join(self._programmingLanguages)

	def printEmployee(self):
		return("Программист " + self.getName() + "(возраст: " + str(self.getAge()) + "; зарплата: " + str(self.getSalary()) + "; языки программирования: " + str(self.getProgrammingLanguages()) + ")")

	def printEmployee(self, url, q, i, edit):
		if edit == True and  'num' in q and i == int(q['num'].value):
			return ("""<tr">
				<td> <select name='typeEmployee'> <option value='Employee'> Работник </option> <option value='Programmer'> Программист </option> </select> </td>
				<td> <input type='text' name='name' value={0}> </td>
				<td> <input type='text' name='age' value={1}> </td>
				<td> <input type='text' name='salary' value={2}> </td>
				<td> <input type='text' name='programmingLanguages' value="{3}"> </td>
				<td colspan=2> <input value='Сохранить' type='submit'> </td>
        		<input value = {4} type="text" name="student" style="display: none;">
        		<input value = {5} type="text" name="select" style="display: none;">
        		<input value = {6} type="text" name="num" style="display: none;">
				</tr>""".format(self.getName(), self.getAge(), self.getSalary(), self.getProgrammingLanguages(), q['student'].value, q['select'].value, q['num'].value)
			)
		else:
			return ("""	<tr>
				<td> Программист </td>
				<td> {0} </td>
				<td> {1} </td>
				<td> {2} </td>
				<td> {3} </td>
				<td> <a href='{4}?student={5}&select=1&num={6}'> Редактировать </a> </td>
				<td> <a href='{4}?student={5}&select=2&num={6}'> Удалить </a> </td>
			</tr>""".format(self.getName(), self.getAge(), self.getSalary(), self.getProgrammingLanguages(), url, q['student'].value, i)
			)