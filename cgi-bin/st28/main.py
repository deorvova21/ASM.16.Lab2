from .company import *

def main(q, selfurl):
	RSU = Company()

	MENU = [
		["Добавить", RSU.add ],
		["Редактировать", RSU.edit ],
		["Удалить", RSU.delete ],
		["Вывести на экран список", RSU.printCompany ],
		["Сохранить", RSU.save ],
		["Загрузить", RSU.load ],
		["Выйти"]
	]

	print ("Content-type: text/html; charset=utf-8\n\n")
	RSU.load()

	if 'select' in q and int(q['select'].value) in range(len(MENU)):
		MENU[int(q['select'].value)][1](selfurl, q)
	else:
		RSU.printCompany(selfurl, q)

def menu(q, selfurl):
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}&select={2}">{3}</a>'.format(selfurl,q['student'].value, i, item[0]))
	print ("------------------------------</pre>");