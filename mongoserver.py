#!/usr/bin/python
# -- coding: utf-8 --
from pymongo import MongoClient
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
port = 0
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("sed -i 's/auth\ =\ true/auth\ =\ false/g' /etc/mongodb.conf")
    os.system("sed -i 's/#auth\ =\ /auth\ =\ /g' /etc/mongodb.conf")
    os.system("service mongodb restart")
    os.system("echo \"db.changeUserPassword('root','%s')\" > /opt/chsql/mongo.sh" % (x))
    pscmd = "sudo netstat -lnpt|grep mongod|awk '{print $4}'"
#    print pscmd
    ipport = os.popen(pscmd).read() 
    print ipport
    os.system("mongo %s --shell /opt/chsql/mongo.sh &" % (ipport))
    os.system("ps -aux|grep mongo\ --shell\ mongo.sh|grep -v grep|awk '{printf $2}'|xargs kill -9")
    os.system("sed -i 's/auth\ =\ false/auth\ =\ true/g' /etc/mongodb.conf")
    os.system("service mongodb restart")
    os.system("echo \" \" > /opt/chsql/mongo.sh")
    return x
def restart():
    os.system("service mongodb restart")
    return 0
def chport(x):
    os.system("echo \"changing port\"")
    os.system("echo \"%s\"" % (x))
    os.system("service mongodb stop")
    os.system("sed -i 's/\(port\ =\).*/\\1/' /etc/mongodb.conf")
    os.system("sed -i 's/port\ =/port\ =\ %s/g' /etc/mongodb.conf" % (x))
    os.system("sed -i 's/#port\ =/port\ =/g' /etc/mongodb.conf")
    os.system("service mongodb start")
    return x
def start():
    os.system("service mongodb start")
    return 0
def stop():
    os.system("service mongodb stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()

