#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import csv
import datetime 


    
FolderName=""
csvfileName=""
ProgBar1=0
ProgBar2=0
   

            
            
from csv import writer
from datetime import datetime
now = datetime.now()
TxtFile=""
if os.path.exists("HSP.txt"):
     
     fh=open("HSP.txt", "r")
    
     for line in fh:  # iterate by-lines over file-like
             try:
                 TxtFile=TxtFile+line.strip('\n')
                 
             except IndexError:  # line has no chars
                 pass  # consider other handling


     fh.close()
    

    
if os.path.exists("HSP.xlsx"):      
   data= pd.read_excel("HSP.xlsx")
   
        
K=data['mutant'] 

for item in K:
    if item[2].isdigit() :
        if item[0]==TxtFile[int(item[1])*10+int(item[2])-1]:
            print (item," Condition OK ---> ", item[0],"==",TxtFile[int(item[1])*10+int(item[2])-1])
        else:
            print (item," Condition Error ---> ", item[0],"==",TxtFile[int(item[1])*10+int(item[2])-1])
            FileStatus='Error'
    else:
        if item[0]==TxtFile[int(item[1])-1]:
            print (item," Condition OK ---> ", item[0],"==",TxtFile[int(item[1])-1])
        else:
            print (item," Condition Error ---> ", item[0],"==",TxtFile[int(item[1])-1])
            FileStatus='Error'
    a=input()       
print('Finished')     


# In[ ]:





# In[ ]:




