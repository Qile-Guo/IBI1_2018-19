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

#my code
x=1750
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
            
print("x"+ "=" + a)



#others'codes
#code1:
n=input("n= ")
st=str(n+" is ")
integer=int(n)
while integer>=1:
    i=0
    while 2**i <= integer:#i increases until reaching the largest i which is small than integer
        i +=1
    i=i-1
    st=st+ "2**"+str(i)+"+"
    integer=integer-2**i
st=st[:-1]#delete the last "+"
print(st)
#the general idea is the same as mine.
#the programmer uses st=st[:-1] to omit the first loop I use, which makes the code simplier.

#code2:
from random import randint
n=randint(0,2**13)#select random integer n
a= str(n)+' is '
for i in range(13):
    x=12-i # x as exponent
    if n> 2**x:  #if n is larger than 2**x, add x
        n=n-2**x
        a+='2**'+str(x)+' + '
        #if n is smaller than 2**x, i=i+1
        #if n is equal to 2**x, end process
    elif n==2**x:
        a+='2**'+str(x)
print(a)
#the general idea is the same as mine.
#the programmer uses x which decreases from 13 to 0 to replace i, which simplifies "x < 2**i and x >= 2**(i-1)".
#She also separate another situation(n==2**x), which will perfectly omit the last "+".
        


