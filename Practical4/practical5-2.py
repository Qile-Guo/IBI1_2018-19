# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:17:51 2019

@author: 94979
"""

test_string=input("give me a string of words ")
backwards = ''.join(reversed(test_string))
l=[]
l=backwards.split()
sortedl = sorted(l)
sortedl.reverse()
print(sortedl)