import os
def loadtpl(fName):
        docrootname = 'PATH_TRANSLATED'
        with open(os.environ[docrootname]+'/cgi-bin/st09/tpl/'+fName+'.tpl', 'rt') as f:
                return f.read()
