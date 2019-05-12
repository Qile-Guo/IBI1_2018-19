# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:17:51 2019

@author: 94979
"""

test_string=input("give me a string of words ")#input the string

l=[]
l=test_string.split(' ') #convert string into list and one word is one item
for i in range(len(l)): #use for loop to reserve every word in l 
    l[i] = l[i][::-1]
"""
Why do not use "for i in l:
 i = i[::-1]"?
Change the i itself instead of creating a new object.

"""
sortedl = sorted(l)
sortedl.reverse()#reverse again 
print(sortedl)

