# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:03 2019

@author: 94979
"""



str1=input("give me a sequence of DNA:")
dict = {}
for n in str1:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
print(str(dict))


import matplotlib.pyplot as plt
sizes = [dict['A'],dict['T'],dict['C'],dict['G']]
labels = ['A','T','C','G']
plt.pie(sizes, labels=labels,autopct='%1.1f%%',shadow=False)
plt.axis('equal')
plt.show
