#!/usr/bin/python
# -- coding: utf-8 --
#5.7 password change to authentication_string
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   
global password
password = "qazxswedc1="
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("service mssql-server stop")
    os.system("/opt/mssql/lib/mssql-conf/set-sa-password.py %s" % (x))
    global password
    password = x
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
def startlog():
    os.system("sqlcmd -S localhost -U sa -P %s -q \"USE master;ALTER DATABASE model SET RECOVERY FULL ;\" &" % (password))
    os.system("service mssql-server restart")
    return 0
def stoplog():
    os.system("sqlcmd -S localhost -U sa -P %s -q \"USE master;ALTER DATABASE model SET RECOVERY SIMPLE ;\" &" % (password))
    return 0
def backup():
    os.system("service mssql-server restart")
    return 0
def restore():
    os.system("service mssql-server restart")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.register_function(startlog)
    sqlRpc.register_function(stoplog)
    sqlRpc.register_function(backup)
    sqlRpc.register_function(restore)
    sqlRpc.serve_forever()
