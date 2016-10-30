import logging

class log():
    def __init__(self):
        logging.basicConfig(filename='./cgi-bin/st35/.log',level=logging.DEBUG,format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s')
    def __call__(self,**args):
        logging.debug(args)
