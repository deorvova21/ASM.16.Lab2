from .kindergarden import Kindergarden
import cgi

def main(q, selfurl):
	
	K = Kindergarden(q, selfurl)
	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'action' in q:
		if (q['action'].value=="1"): 
			K.read()
		if (q['action'].value=="2"):
			K.write()
		if (q['action'].value=="3"):
			K.delete()
	else: 
		K.write()
