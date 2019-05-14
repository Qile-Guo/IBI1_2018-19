# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:55 2019

@author: 94979
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000 # the total population
#use arrays to store changes of susceptible or infected or recovered people
spt = []
ift = []
rcv = []
beta = 0.3
gamma = 0.05
count_ift = 0 
count_rcv = 0 
#initial situation
spt.append(9999)
ift.append(1)
rcv.append(0)

for time in range(1,1001):
    #randomly produce the infected people with probability beta*ift[time-1]/N
    for i1 in np.random.choice(range(2),spt[time-1],p=[1-beta*ift[time-1]/N, beta*ift[time-1]/N]): 
        if i1==1:
          count_ift += 1
    spt.append(spt[time-1]-count_ift)
    #randomly produce the recovered people with probability gamma
    for i2 in np.random.choice(range(2),ift[time-1],p=[1-gamma, gamma]):
        if i2==1:
            count_rcv += 1
    
    rcv.append(rcv[time-1]+count_rcv)
    ift.append(ift[time-1]+count_ift-count_rcv)
    #reset
    count_ift=0
    count_rcv=0

#PLOT
plt.figure(figsize=(6,4),dpi=150)

x=range(0,1001)
plt.plot(x,spt,label='susceptible')
plt.plot(x,ift,label='infected')   
plt.plot(x,rcv,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend() 
plt.savefig('SIR model', type="png")


