# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:03 2019

@author: 94979
"""

"""
counting DNA nucleotides
"""


str1=input("give me a sequence of DNA:")
dict = {}
#if n appears in dict, add 1 to the number. If not, add item to dict and appoint 1 to its number.
for n in str1:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
print(str(dict))

#PIE PLOT
import matplotlib.pyplot as plt
sizes = [dict['A'],dict['T'],dict['C'],dict['G']]
plt.title('pie of the four DNA nucleotides')
colors = ['mistyrose', 'powderblue', 'bisque', 'azure']
labels = ['A','T','C','G']
explode= [0, 0.1, 0, 0]
plt.pie(sizes, labels=labels,autopct='%1.1f%%', colors = colors, explode = explode, startangle = 30,shadow=False)
plt.axis('equal')
plt.show

