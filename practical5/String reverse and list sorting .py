# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:17:51 2019

@author: 94979
"""

test_string=input("give me a string of words ")#input the string
backwards = ''.join(reversed(test_string))#reverse all words
l=[]
l=backwards.split()#convert string into list and one word is one item
sortedl = sorted(l)
sortedl.reverse()#reverse again 
print(sortedl)