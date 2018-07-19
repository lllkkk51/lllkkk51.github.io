#!/usr/bin/python
# -- coding: utf-8 --
#5.7 password change to authentication_string
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os   
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld skip-grant-tables True")
    os.system("service mysqld restart")
    os.system("mysql -uroot -e \"use mysql;update user set password=password(%s) where user='root';flush privileges;\"" % (x))
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld skip-grant-tables False")
    os.system("service mysqld restart")
    return x
def chport(x):
    os.system("service mysqld stop")
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld port %s" % (x))
    os.system("service mysqld start")
    return x
def restart():
    os.system("service mysqld restart")
    return 0
def start():
    os.system("service mysqld start")
    return 0
def stop():
    os.system("service mysqld stop")
    return 0
def startlog():
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld log_bin /opt/chsql/log/mysqlbin.log")
    os.system("service mysqld restart")
    return 0
def stoplog():
    os.system("source /opt/chsql/iniset.sh && iniset -sudo /etc/my.cnf mysqld log_bin ")
    os.system("service mysqld restart")
    return 0
def backup():
    os.system("service mysqld restart")
    return 0
def restore():
    os.system("service mysqld restart")
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
