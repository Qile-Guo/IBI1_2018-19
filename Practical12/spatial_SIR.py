# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:45:09 2019

@author: 94979
"""


'''
pseudo code
I suppose the situation where the infected people are first randomly selected to recover and then use still infected people to infect others.
use 0 for susceptible, 1 for infected, 2 for recovered

import useful libraries
make 100*100 array
randomly select the outbreak
make a dictionary to indicate relative positions of neighbors 

use where() to find the infected people
randomly produce the recovered poeple with probability gamma
change their states from 1 to 2
use where() to find the position of people who are still infected (still 1).
Use (ift[0][i2]+dict[i3][0], ift[1][i2]+dict[i3][1]) to show neighbors position.
infected people randomly infect their neighbors who are not infected or recover from infection and make sure I don't fall off an edge first. 
excute 100 times
Make the plot every time



'''

import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100,100)) # make array of all susceptible population
outbreak = np.random.choice(range(100),2) #randomly select the outbreak 
population[outbreak[0],outbreak[1]] = 1 
#plot of the random selection of one infected individual 
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis',interpolation = 'nearest')

beta = 0.3
gamma = 0.05
dict={0:(-1,1),1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),5:(1,0),6:(1,1),7:(0,1)}


for time in range(1,101):
    ift = np.where(population==1) #find the infected people
    #randomly produce the recovered poeple
    rcv = np.random.choice(range(2),len(ift[0]),p=[gamma,1-gamma]) 
    #change the stage of recovered people,from 1 to 2
    for i1 in range(0,len(ift[0])):
        if rcv[i1]==0:
            population[ift[0][i1],ift[1][i1]]=2
    ift = np.where(population==1) #find the people who are still infected.
    #randomly produce the infected neighbors
    for i2 in range(0,len(ift[0])):
        neighbor = np.random.choice(range(2),8,p=[1-beta,beta])
        for i3 in range(0,8):
            if neighbor[i3] == 1:              
                    if ift[0][i2]+dict[i3][0]>=0 and ift[1][i2]+dict[i3][1]>=0: #make sure I don't fall off an edge
                        try:
                            if population[ift[0][i2]+dict[i3][0], ift[1][i2]+dict[i3][1]] ==0: # only infect people who are not infected or recover. 
                                population[ift[0][i2]+dict[i3][0], ift[1][i2]+dict[i3][1]] = 1 #change the stage of neighbors,from 0 to 1
                        except:
                            pass
   
            
#PLOT
    plt.figure(figsize=(6,4), dpi=150)
    plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
    
