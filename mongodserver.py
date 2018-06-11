#!/usr/bin/python
# -- coding: utf-8 --
#from pymongo import MongoClient
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("sed -i 's/security:/#security:/' /etc/mongod.conf")
    os.system("sed -i 's/authorization:\ enabled//' /etc/mongod.conf")
    os.system("service mongod restart")
##    sqlcmd="db.dropUser('admin');db.createUser({user:\"admin\",pwd:\"" + x + "\",roles:[{role:\"userAdminAnyDatabase\",db:\"admin\"},{role:\"readWriteAnyDatabase\",db:\"admin\"}]})"
    sqlcmd="db.changeUserPassword('admin','" + x + "')"
    print "sqlcmd = " + sqlcmd
##    fw = open("/opt/chsql/mongo.sh", 'w')
    fw = open("/opt/chsql/mo.sh", 'w')
    fw.write(sqlcmd + "\n") 
    fw.close()
    pscmd = "sudo netstat -lnpt|grep mongod|awk '{print $4}'|cut -d \":\" -f2"
    port = os.popen(pscmd).read() 
    port = port.strip("\n")
    print "port = " + port
##    mongocmd = "mongo --port " + port + " --shell mongo.sh &"
    mocmd = "mongo --port " + port + " --shell /opt/chsql/mo.sh &"
##    print "mongocmd = " + mongocmd
    print "mocmd = " + mocmd
##    os.system(mongocmd)
    os.system(mocmd)
#    os.system("ps -aux|grep mongo\ --shell\ mongo.sh|grep -v grep|awk '{printf $2}'|xargs kill -9")
    os.system("sed -i 's/#security:/security:\\n\ \ authorization:\ enabled/' /etc/mongod.conf")
    os.system("service mongod restart")
#    os.system("echo \" \" > /opt/chsql/mongo.sh")
    return x
def restart():
    os.system("service mongod restart")
    return 0
def chport(x):
    os.system("echo \"changing port\"")
    os.system("echo \"%s\"" % (x))
    os.system("service mongod stop")
    os.system("sed -i 's/\(port:\ \).*/\\1/' /etc/mongod.conf")
    os.system("sed -i 's/port:\ /port:\ %s/g' /etc/mongod.conf" % (x))
#    os.system("sed -i 's/#port\ =/port\ =/g' /etc/mongod.conf")
    os.system("service mongod start")
    return x
def start():
    os.system("service mongod start")
    return 0
def stop():
    os.system("service mongod stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()

