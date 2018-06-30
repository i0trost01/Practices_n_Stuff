# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 19:41:08 2018

@author: Ivan Trost
"""
import numpy as np

grid= [[],[],[],[],[],[],[],[]]
for i in range(8):
    grid[0].append(i) 
    grid[1].append(i+8) 
    grid[2].append(i+16)
    grid[3].append(i+24)
    grid[4].append(i+32)
    grid[5].append(i+40)
    grid[6].append(i+48)
    grid[7].append(i+56)
    
grid=np.array(grid)
grid2=np.copy(grid)

def answer(src, dest):
   
    grid[grid==src]=101
    z=list(grid2[np.where(grid==101)])
    
    for i in range(1,6):
        for j in range(0,len(z)):
            if np.where(grid2==z[j])[1]!=0:
                grid[grid2==z[j]+(6)]=101+i
                grid[grid2==z[j]+(15)]=101+i
                grid[grid2==z[j]-(17)]=101+i
                grid[grid2==z[j]-(10)]=101+i
        
            if np.where(grid2==z[j])[1]!=7:
                grid[grid2==z[j]-(6)]=101+i
                grid[grid2==z[j]+(10)]=101+i
                grid[grid2==z[j]-(15)]=101+i
                grid[grid2==z[j]+(17)]=101+i
        
                
        z=list(grid2[np.where(grid==101+i)])
        
    
        if np.where(grid==dest)[0].size==0:
            return(i)   


print(answer(0,1))