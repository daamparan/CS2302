
"""
Created: David Amparan
Instructor: Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
Last Modified:May 5th 2019
"""
import random
import math as mate 
import time as tiempo
import numpy as np
from math import *

def setS(s):
    sum=0
    for i in range(len(s)):
        sum+=s[i]
    return sum


def similar_trigs(trigs,tries=1000,tolerance=0.0001):
    #the trigs is a list of the identities
    temp=trigs
    equalities=[]
    count=0
    while len(trigs)!=0:
        toCompare=trigs.pop(0)
        for i in range(len(temp)):
            for l in range(tries):
                x=random.uniform(-(mate.pi), mate.pi)
                if toCompare is not temp[i]:
                    y1=eval(toCompare)
                    y2=eval(trigs[i])
                    if np.abs(y2-y1)>tolerance:
                        count=count
                    else:
                        count+=1
    return count

def similar_trigs2(user,trigs,tries=1000,tolerance=0.0001):
    count=0
    for i in range(len(trigs)):
        x=random.uniform(-(mate.pi),mate.pi)
        y1=eval(user)
        y2=eval(trigs[i])
        if np.abs(y2-y1)>tolerance:
            count=count
        else:
            count+=1
    return count
    


def partitionSum(S,set1,set2,last):
    #base case
    if setS(set1)==setS(set2) and last<0:
        return True,[],[]
    if setS(set1)!=setS(set2) or last<0:
        return False,[],[]
    #here we created the sets and make our recursive call
    set1.append(S[last])
    #take the last
    res,set1,set2=partitionSum(S,set1,set2,last-1)
    if res:
        return True,set1,[]
    else:
        set2.append(S[last])
        return True,[],set2

functions=['sin(x)','cos(x)','tan(x)','1/cos(x)','-sin(x)','-cos(x)','-tan(x)','sin(-x)','cos(-x)','tan(-x)','sin(x)/cos(x)','2*sin(x/2)*cos(x/2)','sin(x)*sin(x)','1-(cos(x)*cos(x))','(1-cos(2*x))/2','1/cos(x)']
total=similar_trigs(functions)
print("Total Similarities Found:",total)

S=[2,4,5,9,12]
set1=[]
set2=[]
res, set1, set2=partitionSum(S,[],[],len(S)-1)
print(res,set1,set2)


