# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:02:56 2018

@author: Ivan Trost
"""

import math 
prime = [0]*10005
Not_Prime=False
k=0


for i in range (2, 20221):
    for j in range (2, int(math.sqrt(i))+1):
           if i%j==0:
               Not_Prime=True
    if Not_Prime==False:
        for l in range(0,len(str(i))):
            prime[k]=list(str(i))[l]
            k=k+1
    Not_Prime=False
    
prime[10004]=2                   
    


response=[0]*5

def answer(n):
    for i in range(0,5):
        response[i]=prime[n+i]
    response2="".join(str(j) for j in response)
    print(response2)

answer(0)