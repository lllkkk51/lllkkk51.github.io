#!/usr/bin/python
# -- coding: utf-8 --
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("echo \"%s\"" % (x))
    os.system("su - postgres -l -c \"sed -i 's/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\tmd5/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\ttrust/g' /var/lib/pgsql/9.6/data/pg_hba.conf\"")
    os.system("service postgresql-9.6 restart")
    pscmd = "sudo netstat -lnpt|grep postmaster|grep tcp\ |awk '{print $4}'|cut -d ':' -f2"
#    print pscmd
    port = os.popen(pscmd).read()
    port = port.strip("\n")
    print port
    os.system("su - postgres -l -c \"psql -p %s --c \\\"ALTER USER postgres WITH PASSWORD '%s';\\\"\""% (port,x))
    os.system("su - postgres -l -c \"sed -i 's/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\ttrust/host\\tall\\t\\tall\\t\\t0.0.0.0\/0\\t\\tmd5/g' /var/lib/pgsql/9.6/data/pg_hba.conf\"")
    os.system("service postgresql-9.6 restart")
    return x
def chport(x):
    os.system("echo \"changing port\"")
    os.system("echo \"%s\"" % (x))
    os.system("su - postgres -l -c \"sed -i 's/\(port\ =\).*/\\1/' /var/lib/pgsql/9.6/data/postgresql.conf\"")
    os.system("su - postgres -l -c \"sed -i 's/port\ =/port\ =\ %s/g' /var/lib/pgsql/9.6/data/postgresql.conf\"" % (x))
    os.system("su - postgres -l -c \"sed -i 's/#port\ =/port\ =/g' /var/lib/pgsql/9.6/data/postgresql.conf\"")
    os.system("service postgresql-9.6 restart")
    return x
def restart():
    os.system("service postgresql-9.6 restart")
    return 0
def start():
    os.system("service postgresql-9.6 start")
    return 0
def stop():
    os.system("service postgresql-9.6 stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()
