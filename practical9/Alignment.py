# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:18:01 2019

@author: 94979
"""


import os
os.chdir(r'D:/test/IBI1_2018-19/practical9') 

#Read three sequences from .txt files
import re
h = open('seq_human.txt')
seq_human = h.read()
h.close()

m = open('seq_mouse.txt')
seq_mouse = m.read()
m.close()
       
r = open('seq_random.txt')
seq_random = r.read()
r.close()
        
#make the matrix dictionary
blosum = open('BLOSUM62.txt')
blosum62 = {}
data = blosum.readlines() 
letter = re.findall('[A-Z*]', data[0]) # extract all letters or *
blosum.close()

for i in range(0, len(letter)): # i is the location of the first letter
    for j in range(1,len(data)):
        #find the value(postive and negative) with corresponding letters or * and convert them into integer to make the matrix dictionary
        blosum62[(letter[i],data[j][0])] = int(data[j][3*i+2 : 3*i+4]) 


#Compare equences

#-----compare mouse and human sequence--------------------
score = 0
different = 0
subseq = ''
for i in range(0, len(seq_human)):
    if seq_human[i] != seq_mouse[i]:
        different += 1
        sco= blosum62[(seq_human[i],seq_mouse[i])]
        if sco > 0:
            subseq += '+'
        else:
            subseq += '_'
    else:
        subseq +=seq_human[i]
    score += blosum62[(seq_human[i],seq_mouse[i])] #calculate BLOSUM score

normalized_score = score/len(seq_human)#calculate the score which is normalized to sequence length. 
identity_percentage= str(100*(1-different/len(seq_human))) + '%'

print('SOD2_human (NP_000627.2)')
print(seq_human) 
print('\nSOD2_mouse (NP_038699.2)')
print(seq_mouse)
print('\nalignment')
print(subseq) #I found although alignment was successfully printed, there was always strange space  before '+' and I had no idea of how to solve it.
print('\nBLOSUM62 raw score:', score)
print('BLOSUM62 normalized score:', normalized_score)
print('Identity:',identity_percentage )

#-----compare mouse and random sequence--------------------
score = 0
different = 0
subseq = ''
for i in range(0, len(seq_random)):
    if seq_random[i] != seq_mouse[i]:
        different += 1
        sco= blosum62[(seq_random[i],seq_mouse[i])]
        if sco > 0:
            subseq += '+'
        else:
            subseq += '_'
    else:
        subseq +=seq_mouse[i]
    score += blosum62[(seq_random[i],seq_mouse[i])] #calculate BLOSUM score

normalized_score = score/len(seq_mouse)#calculate the score which is normalized to sequence length. 
identity_percentage= str(100*(1-different/len(seq_mouse))) + '%'

print('\nRandomSeq')
print(seq_random) 
print('\nSOD2_mouse (NP_038699.2)')
print(seq_mouse)
print('\nalignment')
print(subseq) #I found although alignment was successfully printed, there was always strange space  before '+' and I had no idea of how to solve it.
print('\nBLOSUM62 raw score:', score)
print('BLOSUM62 normalized score:', normalized_score)
print('Identity:',identity_percentage )

#----compare random and human sequence--------------------
score = 0
different = 0
subseq = ''
for i in range(0, len(seq_human)):
    if seq_human[i] != seq_random[i]:
        different += 1
        sco= blosum62[(seq_human[i],seq_random[i])]
        if sco > 0:
            subseq += '+'
        else:
            subseq += '_'
    else:
        subseq +=seq_human[i]
    score += blosum62[(seq_human[i],seq_random[i])] #calculate BLOSUM score

normalized_score = score/len(seq_human)#calculate the score which is normalized to sequence length. 
identity_percentage= str(100*(1-different/len(seq_human))) + '%'

print('\nSOD2_human (NP_000627.2)')
print(seq_human) 
print('\nRandomSeq')
print(seq_random)
print('\nalignment')
print(subseq) #I found although alignment was successfully printed, there was always strange space  before '+' and I had no idea of how to solve it.
print('\nBLOSUM62 raw score:', score)
print('BLOSUM62 normalized score:', normalized_score)
print('Identity:',identity_percentage )








