from .hospital import *
import cgi

def main(q, selfurl):
	hosp = Hospital(q, selfurl)
	MENU = {
		'display': hosp.display,
		'print_list': hosp.print_list,
		'delete': hosp.delete,
		'edit': hosp.edit,
		'add_patient': hosp.add_patient,
		'add_diagnosis': hosp.add_diagnosis,
		'clear': hosp.clear
	}
	print ("Content-type: text/html; charset=utf-8\n\n")
	if 'act' in q:
		MENU[q['act'].value]()
	else:
		MENU['display']()
