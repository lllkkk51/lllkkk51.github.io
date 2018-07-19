#!/usr/bin/python
import sys
from xmlrpclib import ServerProxy
if __name__ == '__main__':
    s = ServerProxy("http://%s:8686" % (sys.argv[1]))
    print s.backup()
