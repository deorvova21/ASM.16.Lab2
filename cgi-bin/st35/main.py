from .group import group
from .view import view
from .controller import Controller

def main(q, selfurl):
	controller = Controller(q, selfurl)
	print("Content-type: text/html; charset=utf-8\n")

	controller.main()

	#group(q, selfurl).f()
