import os
def LoadTpl(fName):
        docrootname = 'PATH_TRANSLATED'
        with open(os.environ[docrootname]+'/cgi-bin/st07/tpl/'+fName+'.tpl', 'rt') as f:
                return f.read()
