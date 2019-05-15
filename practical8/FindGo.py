# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:46:06 2019

@author: 94979
"""

import xml.dom.minidom
import re
import pandas as pd

#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])


#Function to find childnodes 
def Child(id, resultSet):
    for i in terms:
        parents = i.getElementsByTagName('is_a')
        geneid = i.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(geneid)
                Child(geneid, resultSet)
                


# use DOM to present an XML document as a tree structure   
DOMTree = xml.dom.minidom.parse('go_obo.xml') 
Ontology = DOMTree.documentElement 
terms = Ontology.getElementsByTagName("term")

#check and find term related to autophagosome
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    re_aut = re.compile(r'autophagosome')
    if re_aut.search(defstr):
        id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        resultSet = set()
        Child(id, resultSet)#use Child(id, resultSet) to find the number of childnodes for term related to autophagosome
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]}))#store results 
        print(id, len(resultSet))

#save to excel
df.to_excel('autophagosome.xlsx',index=False)