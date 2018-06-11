#!/usr/bin/python
# -- coding: utf-8 --
from SimpleXMLRPCServer import SimpleXMLRPCServer
import os
import time
def chpassword(x):
    os.system("echo \"changing password\"")
    os.system("sed -i 's/\(requirepass\ \).*/\\1%s/' /root/redis-4.0.9/redis.conf" %(x))
    os.system("sed -i 's/#\ requirepass\ /requirepass\ /' /root/redis-4.0.9/redis.conf")
    os.system("ps -aux|grep redis-server|grep -v grep|awk '{print $2}'|xargs kill -9")
    os.system("/root/redis-4.0.9/src/redis-server /root/redis-4.0.9/redis.conf")
    return x
def restart():
    os.system("ps -aux|grep redis-server|grep -v grep|awk '{print $2}'|xargs kill -9")
    os.system("/root/redis-4.0.9/src/redis-server /root/redis-4.0.9/redis.conf")
    return 0
def chport(x):
    os.system("echo \"changing port\"")
    os.system("sed -i 's/\(port\ \).*/\\1%s/' /root/redis-4.0.9/redis.conf" %(x))
    os.system("ps -aux|grep redis-server|grep -v grep|awk '{print $2}'|xargs kill -9")
    os.system("/root/redis-4.0.9/src/redis-server /root/redis-4.0.9/redis.conf")
    return x
def start():
    os.system("/root/redis-4.0.9/src/redis-server /root/redis-4.0.9/redis.conf")
    return 0
def stop():
    os.system("ps -aux|grep redis-server|grep -v grep|awk '{print $2}'|xargs kill -9")
    return 0
if __name__ == '__main__':
    sqlRpc = SimpleXMLRPCServer(('0.0.0.0', 8686))
    sqlRpc.register_function(chpassword)
    sqlRpc.register_function(restart)
    sqlRpc.register_function(chport)
    sqlRpc.register_function(start)
    sqlRpc.register_function(stop)
    sqlRpc.serve_forever()
