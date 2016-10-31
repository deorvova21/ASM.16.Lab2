import cgi, cgitb, os, sys, codecs

cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())

import st00.main
import st04.main
import st05.main
import st06.main
import st07.main
import st08.main
import st10.main
import st11.main
import st12.main
import st13.main
import st15.main
import st16.main
import st18.main
import st19.main
import st22.main
import st24.main
import st27.main
import st35.main
import st28.main
import st37.main
import st40.main
import st41.main
import st46.main
#	добавить импорт своего модуля по шаблону 
#	import st<номер по журналу>.main


MENU = [
        ["[00] Образец", st00.main.main],
        ["[04] Багаутдинов", st04.main.main],
		["[05] Беккер", st05.main.main],
		["[06] Беков", st06.main.main],
        ["[07] Бурлакова", st07.main.main],
        ["[08] Гаврилова", st08.main.main],
        ["[10] Гуцев", st10.main.main],
        ["[11] Гюльназарян", st11.main.main],
		["[12] Дворянчиков", st12.main.main],
        ["[13] Димитриев", st13.main.main],
        ["[15] Иванов", st15.main.main],
        ["[16] Игнатьева", st16.main.main],
		["[18] Колесникова Анастасия", st18.main.main],
        ["[19] Колесникова Анна", st19.main.main],
        ["[22] Короленко", st22.main.main],
        ["[24] Кутикова", st24.main.main],
        ["[27] Можайкин", st27.main.main],
        ["[28] Мурадян", st28.main.main],
		["[35] Симкин", st35.main.main],
        ["[37] Трифонов", st37.main.main],
        ["[40] Ягелло", st40.main.main],
        ["[41] Якупова", st41.main.main],
        ["[46] Левченко", st46.main.main]
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
