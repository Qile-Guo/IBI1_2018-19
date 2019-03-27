# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:03 2019

@author: 94979
"""


#method1
str1=input("give me a sequence of DNA:")
dict = {}
#if n appears in dict, add 1 to the number. If not, add item to dict and appoint 1 to its number.
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

#method2
DNA = "ATTCCGGGG"
DNA = list(DNA) #actually this line can be deleted.
myDict = {}
for word in DNA:
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1
text = input(myDict)
#the general idea is the same as mine.

#method3
a = 0
t = 0
c = 0
g = 0
text = input("give me a sequence of DNA:")
dna = list(text) #put the input into list
while len(dna) > 0:
    i = dna.pop() #extract the last item and delete it
    if i=="A":
        a=a+1
    elif i=="T":
        t=t+1
    elif i=="C":
        c=c+1
    else:
        g=g+1
dict = {"A":a,"T":t,"C":c,"G":g}
print(dict)
#the programmer uses the list first and finally store the value in dictionary. The key is the code"i = dna.pop()".
