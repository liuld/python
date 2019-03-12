#!/usr/local/python36/bin/python3
# _*_ coding: utf-8 _*_

import string, random

def Pwd(num):
    str = string.digits + string.ascii_letters + string.punctuation
    pwd_str = []
    for i in range(0,num):
        pwd_str.append(random.choice(str))
    return ''.join(pwd_str)

if __name__ == '__main__':
    try:
        num = int(input("please input a num:"))
    except Exception as e:
        num = 8 
    print(Pwd(num))
