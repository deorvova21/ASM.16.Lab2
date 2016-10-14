import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st04.main
import st05.main
import st24.main
import st28.main
import st37.main
import st40.main
#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main


MENU = [
        ["[00] Образец", st00.main.main],
        ["[04] Багаутдинов", st04.main.main],
		["[05] Беккер", st05.main.main],
        ["[24] Короленко", st24.main.main],
        ["[28] Мурадян", st28.main.main],
        ["[37] Трифонов", st37.main.main],
        ["[40] Ягелло", st40.main.main]
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<номер по журналу>] <Фамилия>", <ссылка на функцию>],
	]


def menu(selfurl):
	print ("Content-type: text/html; charset=utf-8\n\n")
	print ('<pre>------------------------------');
	for i, item in enumerate(MENU):
		print('<a href="{0}?student={1}">{2}</a>'.format(selfurl, i+1, item[0]))
	print ("------------------------------</pre>");


def main():
	q = cgi.FieldStorage()
	selfurl = os.environ['SCRIPT_NAME']
	st = int(q.getvalue('student', 0))
	if st > 0 and st <= len(MENU):
		MENU[st-1][1](q, selfurl)
	else:
		menu(selfurl)

main()
