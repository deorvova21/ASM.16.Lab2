from .Store import *
import cgi

def main(q, selfurl):
	
	st=Store(q, selfurl)
	
	print ("Content-type: text/html; charset=utf-8\n\n")
	
	if 'selection' in q:
		if (q["selection"].value=="1"): 
			st.new_()
		if (q["selection"].value=="2"):
			st.print_()
		if (q["selection"].value=="3"):
			st.delete()
		if (q["selection"].value=="4"):
                        st.clear()
	else: 
		st.print_()
