
"""
Author: David Amparan
Last Modified on:Apr 13, 2019
Instructor: Fuentes, Olac
T.A: Anindita Nath, Maliheh Zargaran
Purpose: Lab 6 serves the purpose of putting disjoint set forests
into practice by helping us create a maze. This maze will be formed when each
item within itis part of a set
"""
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import interpolate 


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri
"""
Method Name: numberSets | Parameters: DSF
Functionality: Will return the number of sets within the DSF
"""
def numberSets(DSF):
    #we will traverse entire list to find the -1
    numSets=0
    for i in range(len(DSF)):
        if DSF[i]==-1:
            numSets+=1
    return numSets

"""
Method Name:checkSameSet | Parameters:DSF, walls
Functionality: Checking the given walls within the DSF to 
determine if they are within the same set; if they are not
return true 
"""
def checkSameSet(DSF,walls):
    same=False
    if find(DSF,walls[1]) == find(DSF,walls[0]):
        same=True
    return same


print("-------------------Lab 6-------------------")
print("For this lab a maze will be drawn, while")
print("we still have more than 1 set in the DSF")
print("we will keep constructing the maze")
print("by either regular union and then size")
print("compression union.")

m = int(input("Enter the rows: "))
n = int(input("Enter the columns: "))
userChoice=int(input("Enter 1 for union and 2 for union compression: "))
#create the dsf
DSF = DisjointSetForest(m*n)
plt.close("all") 
walls = wall_list(m,n)

"""
for i in range(len(walls)//2): #Remove 1/2 of the walls 
    d = random.randint(0,len(walls)-1)
    print('removing wall ',walls[d])
    walls.pop(d)

draw_maze(walls,m,n)
"""
if userChoice==1:
    #application for regular union
    draw_maze(walls,m,n,cell_nums=True) 
    while numberSets(DSF)>1:
        #here we attain the random walls
        d=random.randint(0,len(walls)-1)    
        if checkSameSet(DSF,walls[d])==False:
            union(DSF, walls[d][0], walls[d][1])
            walls.pop(d)
    draw_maze(walls,m,n)
    
elif userChoice==2:
    #application for compression size
    draw_maze(walls,m,n,cell_nums=True) 
    while numberSets(DSF)>1:
        d=random.randint(0,len(walls)-1)    
        if checkSameSet(DSF,walls[d])==False:
            union_c(DSF,walls[d][0],walls[d][1])
            walls.pop(d)
    draw_maze(walls,m,n)
        
        