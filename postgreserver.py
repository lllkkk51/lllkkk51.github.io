#!/usr/bin/python
# -- coding: utf-8 --
from pymongo import MongoClient
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
port = 0
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("echo \"%s\"" % (x))
    os.system("su - postgres && sed -i 's/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\tmd5/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\ttrust/g' /var/lib/pgsql/9.3/data/pg_hba.conf")
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl restart")
    os.system("su - postgres && psql -e  \"ALTER USER postgres WITH PASSWORD '%s';\"" % (x))
    os.system("su - postgres && sed -i 's/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\ttrust/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\tmd5/g' /var/lib/pgsql/9.3/data/pg_hba.conf")
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl restart")
    return x
def chport(x):
    os.system("echo \"changing port\"")
    os.system("echo \"%s\"" % (x))
    os.system("su - postgres && sed -i 's/\(port\ =\).*/\\1/' /var/lib/pgsql/9.3/data/pg_hba.conf")
    os.system("su - postgres && sed -i 's/port\ =/port\ =\ %s/g' /var/lib/pgsql/9.3/data/pg_hba.conf" % (x))
    os.system("su - postgres && sed -i 's/#port\ =/port\ =/g' /var/lib/pgsql/9.3/data/pg_hba.conf")
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl restart")
    return x
def restart():
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl restart")
    return 0
def start():
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl start")
    return 0
def stop():
    os.system("su - postgres && /usr/pgsql-9.3/bin/pg_ctl stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()
