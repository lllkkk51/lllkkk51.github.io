#!/usr/bin/python
# -- coding: utf-8 --
#5.7 password change to authentication_string
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("service mssql-server stop")
    os.system("/opt/mssql/lib/mssql-conf/set-sa-password.py %s" % (x))
    os.system("service mssql-server restart")
    return x
def chport(x):
    os.system("echo \"changing port\"")
    os.system("/opt/mssql/bin/mssql-conf set network.tcpport %s" % (x))
    os.system("service mssql-server restart")
    return x
def restart():
    os.system("service mssql-server restart")
    return 0
def start():
    os.system("service mssql-server start")
    return 0
def stop():
    os.system("service mssql-server stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()
