from .controller import Controller

def main(q, selfurl):
	controller = Controller(q, selfurl)
	print("Content-type: text/html; charset=utf-8\n")
	controller.main()


