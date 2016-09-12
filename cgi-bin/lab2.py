import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main


MENU = [
        ["[00] Образец", st00.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]


def menu(selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	i = 0;
	print ('<pre>------------------------------');
	for item in MENU:
		print('<a href="{0}?student={1}">{2}</a>'.format(selfurl, i+1, item[0]))
		i += 1
	print ("------------------------------</pre>");


def main():
	q = cgi.FieldStorage()
	st = 0
	selfurl = os.environ['SCRIPT_NAME']
	if 'student' in q:
		st = 0+int(q['student'].value)
	if st > 0 and st <= len(MENU):
		MENU[st-1][1](q, selfurl)
	else:
		menu(selfurl)

main()
