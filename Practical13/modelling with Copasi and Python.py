# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:17:35 2019

@author: 94979
"""

import os
os.chdir(r'D:\test\IBI1_2018-19\Practical13')
import re
import numpy
import matplotlib.pyplot as plt
import xml.dom.minidom

names=[]
content=[]
results=[]
k_predator_breeds=0.02
k_predator_dies=0.4
k_prey_breeds=0.1
k_prey_dies=0.2

#-------------change the parameter value in convert predator-prey.xml-----------

  
DOMTree = xml.dom.minidom.parse ("predator-prey.xml")
Ontology = DOMTree.documentElement 
parameters = Ontology.getElementsByTagName("parameter")

pm = {}
for i in range(0,4):
    parameter = numpy.random.sample()
    parameter_name = parameters[i].getAttribute('id')
    pm[parameter_name]=parameter
    print(parameter_name,':',parameter)
    parameters[i].setAttribute('value',str(parameter))#change the value

#save the changes 
filexml = open('predator-prey.xml','w')
DOMTree.writexml(filexml)
filexml.close()

#----------------convert predator-prey.xml into predator-prey.cps----------------
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding="utf-8")
    cpsTree.writexml(cpsFile)
    cpsFile.close()

xml_to_cps()

#------------get simulation results------------------------------
os.system("CopasiSE.exe D:/test/IBI1_2018-19/Practical13/predator-prey.cps")

#------------Read simulation results-----------------------------
names=[]
content=[]
results=[]
fhand=open(r'D:/test/IBI1_2018-19/Practical13/modelResults.csv')
read=fhand.read()

All = re.split(r',|\n',read)
del(All[-1])#delete the last unnecessary space

for i in range(0,len(All),3):
    content.append((All[i],All[i+1],All[i+2]))
names.append(content[0])
results = content[1:] 

results = numpy.array(results)
results = results.astype (numpy.float)

#----------------------PLOT---------------------
plt.figure()
plt.figure(figsize=(6,4),dpi=150)
x1=range(0,201)
plt.plot(x1,results[:,1],label='Predator (b=' + str(pm['k_predator_breeds']) + ', d=' + str(pm['k_predator_dies']) + ')')
plt.plot(x1,results[:,2],label='Prey (b=' + str(pm['k_prey_breeds']) + ', d=' + str(pm['k_prey_dies']) + ')')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend(loc=1)#make the legend on the upper right

plt.figure()
plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,1],results[:,2])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')

#pseudocode for TASK6
#Use the for loop on the begining to change parameters and run a simulation several times

#Output time course and limit cycle figures every time
#Store 4 parematers and two figures into one file every time

#Output the maximum number of predator in your simulation
#Use max() to find the maximum number of predators for every simulation and record the maximum in the list
#Use max() again to find the maximum number in the mentioned list
#Print the maximum number
#Use the same method to output the minimum of prey with min()

#Output whether your prey dies out during the course of the simulation
#Use if statement to judge whether the number of prey equal 0(results[i,2] != 0) for every prey number(use for loop) 
#If there is the number of prey equalling 0, print('there is prey dying out during the course of the simulation')
#If there is no number of prey equalling 0, print('there is not prey dying out during the course of the simulation')
#Also we can use the minimum of prey calculated before to judge whether your prey dies out during the course of the simulation (if there is prey dying out during the course of the simulation, the minimum of prey will be 0 )


