import os

def load(file):
        docrootname = 'PATH_TRANSLATED'
        with open(os.environ[docrootname]+'/cgi-bin/st17/tpl/'+file+'.tpl', 'rt') as f:
                return f.read()
