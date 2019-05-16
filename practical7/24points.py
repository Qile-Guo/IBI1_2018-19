# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:59:18 2019

@author: 94979
"""

import re
from fractions import Fraction
re_numtest = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)') 
i = 1

#--------------make sure the input numbers must be interger between 1 and 23-----------

while i:
    i=0
    number = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numList = number.split(',')
    for j in range(0,len(numList)):
        if 0 < float(numList[j]) < 24 and float(numList[j]) == int(float(numList[j])):
            continue
        else:
            print('The input number must be integers from 1 to 23')
            i=1
            break

num = list(map(int,numList))  
count = 0 #count the recursion time

#-------------define function---------------------------
#n is len(num) 
def dfs(n):
    global count #assign the value to the variable which is not in the dfs(n) function.
    count = count +1
    
    if n == 1:
        if(float(num[0])==24):
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]            
            num[i] = a+b
            
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a: # avoid situation where denominator will be 0
                #floats are not precise
                num[i] = Fraction(b,a)
                if(dfs(n-1)): 
                    return 1 
                
            if b: # avoid situation where denominator will be 0
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            #Backtracking  
            num[i] = a
            num[j] = b
    return 0 

#-----------print the result----------------------
if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)