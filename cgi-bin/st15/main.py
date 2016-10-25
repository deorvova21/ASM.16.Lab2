from .func import Function
import cgi

def main(q, selfurl):
	
	Func = Function(q, selfurl)
	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'action' in q:
		if (q['action'].value=="1"): 
			Func.read()
		if (q['action'].value=="2"):
			Func.write()
		if (q['action'].value=="3"):
			Func.delete()
	else: 
		Func.write()
