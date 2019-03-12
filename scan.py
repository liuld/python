#!/usr/local/python36/bin/python3
# _*_ coding: utf-8 _*_

import threading
import os

def ping(ip):
    res = os.system("ping -c2 %s &> /dev/null" % ip)
    if res:
        print("host %s is down\n" % ip)
    else:
        print("host %s is live\n" % ip)

if __name__ == '__main__':
    for i in range(1,255):
        ip = '192.168.1.%d' % i
        t = threading.Thread(target=ping, args=[ip])
        t.start()
