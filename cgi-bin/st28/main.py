from .company import *

def add(company, selfurl, q):
	if 'typeEmployee' in q:
		typeEmployee = q['typeEmployee'].value

		name = q['name'].value if 'name' in q else ''
		age = q['age'].value if 'age' in q else ''
		salary = q['salary'].value if 'salary' in q else ''
		programmingLanguages = q['programmingLanguages'].value if 'programmingLanguages' in q else ''

		company.add(typeEmployee, name, age, salary, programmingLanguages)
		company.save()
		show(company, selfurl, q)
	else:
		show(company, selfurl, q)
		print ("""<tr">
			<td> <select name='typeEmployee'> <option value='Employee'> Работник </option> <option value='Programmer'> Программист </option> </select> </td>
			<td> <input type='text' name='name'> </td>
			<td> <input type='text' name='age'> </td>
			<td> <input type='text' name='salary'> </td>
			<td> <input type='text' name='programmingLanguages'> </td>
			<td colspan=2> <input value='Сохранить' type='submit'> </td>
        	<input value = {0} type="text" name="student" style="display: none;">
        	<input value = {1} type="text" name="select" style="display: none;">
			</tr>""".format(q['student'].value, q['select'].value)
		)
	

def edit(company, selfurl, q):
	edit = True
	if 'typeEmployee' in q:
		typeEmployee = q['typeEmployee'].value

		num = int(q['num'].value) if 'num' in q else ''
		name = q['name'].value if 'name' in q else ''
		age = q['age'].value if 'age' in q else ''
		salary = q['salary'].value if 'salary' in q else ''
		programmingLanguages = q['programmingLanguages'].value if 'programmingLanguages' in q else ''

		company.edit(typeEmployee, num, name, age, salary, programmingLanguages)
		company.save()
		edit = False

	show(company, selfurl, q, edit)

def delete(company, selfurl, q):
	company.delete(int(q['num'].value))
	company.save()
	show(company, selfurl, q)

def show(company, selfurl, q, edit = False):
	company.printCompany(selfurl, q, edit)

def save(company, selfurl, q):
	company.save()

def load(company, selfurl, q):
	company.load()

MENU = [
	["Добавить", add ],
	["Редактировать", edit ],
	["Удалить", delete ],
	["Вывести на экран список", show ],
	["Сохранить", save ],
	["Загрузить", load ],
	["Выйти"]
]

def main(q, selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	RSU = Company()
	RSU.load()

	if 'select' in q and int(q['select'].value) in range(len(MENU)):
		MENU[int(q['select'].value)][1](RSU, selfurl, q)
	else:
		show(RSU, selfurl, q)

def menu(q, selfurl):
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}&select={2}">{3}</a>'.format(selfurl,q['student'].value, i, item[0]))
	print ("------------------------------</pre>");