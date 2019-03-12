#!/usr/local/python36/bin/python3
# _*_ coding: utf-8 _*_
# 斐波那契数列

ran_num = int(input("please input a range number:"))

fib = [0, 1]
for i in range((ran_num -2)):
    fib.append(fib[-1] + fib[-2])
print(fib)

a = 0
b = 1
fibs = []

while a < 20:
    fibs.append(a)
    a,b = b,a+b
print(fibs)
