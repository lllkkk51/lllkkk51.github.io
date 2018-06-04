#!/usr/bin/python
# -- coding: utf-8 --
from pymongo import MongoClient
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
port = 0
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("sed -i 's/\(requirepass\ \).*/\1%s/' /root/redis-4.0.9/redis.conf" %(x))
    os.system("sed -i 's/#requirepass\ /requirepass\ /' /root/redis-4.0.9/redis.conf")
    os.system("/root/redis-4.0.9/src/redis-server restart")
    return x
def restart():
    os.system("/root/redis-4.0.9/src/redis-server restart")
    return 0
def chport(x):
    os.system("echo \"changing port\"")
    os.system("sed -i 's/\(port\ ).*/\\1%s/' /etc/redis/redis.conf" %(x))
    os.system("/root/redis-4.0.9/src/redis-server start")
    return x
def start():
    os.system("/root/redis-4.0.9/src/redis-server start")
    return 0
def stop():
    os.system("/root/redis-4.0.9/src/redis-server stop")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()
