# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:11:01 2019

@author: 94979
"""
#input x
#first find a power n1 whose 2^n  just smaller than x
#let the x minus 2^n be y
#repeat the last two steps and find n2
#repeat to find n1,n2,n3…until nx=1
#output the result"x= 2**n1 +2**n2 + … +2**1


x=1750
orignx=x # to store the original input 
#use for loop to creat first "2**x" which is different from the rest.
for i in range(1,14):
    if x < 2**i and x >= 2**(i-1):#identify the largest (i-1) which is small than x.
        a='2**'+ str(i-1)
        x= x-2**(i-1)
while x != 0:#identify every i in range(1,14) until it is reduced to 0.
    for i in range(1,14):
        if x < 2**i and x >= 2**(i-1):
            a=a + '+' '2**'+ str(i-1)
            x= x-2**(i-1)

print(str(orignx) + "=" + a)


