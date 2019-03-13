# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:38:12 2019

@author: 94979
"""
x=5
#randomly enter a number
print(x)
while x != 1:
    #use the for-loop to ensure the result ends with1
    if x%2 == 0:
        #x is even
        x=x/2 
    elif x%2 == 1:
        #x is odd
        x=x*3+1
    print(x)

    
    