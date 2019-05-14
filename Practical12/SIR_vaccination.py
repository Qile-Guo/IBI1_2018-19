# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:54:21 2019

@author: 94979
"""


import numpy as np
import matplotlib.pyplot as plt

N = 10000 # the total population
#use arrays to store changes of susceptible or infected or recovered people
spt = []
ift = []
rcv = []
I=[]
beta = 0.3
gamma = 0.05
count_ift = 0 
count_rcv = 0 
rcv=[0]


vac = np.linspace(0, 1, 11)

for i in vac:
    if i==1: #all people are vaccinated 
        spt=[0]
        ift=[0] 
    else:
        S = N - int(i*N)
        spt=[S-1]# one person infected at start
        ift=[1]
        
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
    
    I.append(ift)



#PLOT
plt.figure(figsize=(6,4),dpi=150)
x = range(0,1001)
for i in range(0,len(I)):
    plt.plot(x, I[i],label = str(i*10)+'%')  #plot with different percentages of vaccinated people
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend() 
plt.savefig('SIR model with different vaccination rates', type="png")


