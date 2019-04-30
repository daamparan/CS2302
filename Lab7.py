"""
Author: David Amparan
Instructor: Dr. Fuentes, Olac
TA: 
Purpose: For lab #7 we will use what we did on lab #6 and transfer that DSF representation
into a graph representation of the maze. When this is done we will find 
a Minimum spanning tree with 3 seperate algorithms
"""
import GraphCode
import dsf
import time as tiempo
import Lab6
import random
import matplotlib.pyplot as plt

"""
Method Name: toAL| Parameters: Maze | Return: AL
Functionality: As we take in the maze as a DSF we create a 
AL from the 
"""
def to_AList(forest):
    toReturn=[]
    for i in range(len(forest)):#we check each index with the others to find connections
        add=[]
        for l in range(len(forest)):#if they belong in the same set then we add them to the list for that vertex
            if i == l:
                add=[]
            elif dsf.find(forest,i) == dsf.find(forest,l):
                add.append(l)
        toReturn.append(add)
    return toReturn

"""
Method Name: breathFS | Parameters: AL |
Functionality: Will determine if there is a path from 0 to walls-1
"Which is the end", and it will return a list that contains the path
"""
def breathFS(AL):
    queue=[]
    previous=[] #we will implement the queue as our holding then names speak for themselvs
    queue.append(0)#we can hardcode zero since this is the beginning
    previous.append(0)
    #here we begin traversing our graph 
    while queue != []:
        visited=queue.pop(0)
        for i in AL[visited]:
            if not previous.__contains__(i):
                queue.append(i)
                previous.append(i)
    return previous

"""
Method Name: depthFS | Parameters: AL
Functionality: Depth first search will perform like i said, a depth first search
and return an array with the path found
"""
def depthFS(AL):
    stack=[]
    previous=[]
    #we want to start at 0 so we hard code it
    stack.append(0)
    while stack != []:#while our stack is not empty
        current=stack.pop()
        if not previous.__contains__(current):
            previous.append(current)
            for i in AL[current]:
                stack.append(i)
    return previous
            
"""
Method Name: depthFS | Parameters: AL
Functionality: Depth first search will perform like i said, a depth first search
and return an array with the path found, this is a recursive method however 
"""            
def depthFSRecur(AL,current=0,previous=[]):
    if not previous.__contains__(current):
        previous.append(current)
    for i in AL[current]:
        depthFSRecur(AL,i,previous)
    return previous
    
        


print("--------------Lab 7-------------------")
print("Graph Representation of a Maze")

rows=int(input("Enter the number of rows wanted: "))
columns=int(input("Enter the number of columns wanted: "))
toRemove=int(input("Enter the number of walls you wish to remove: "))
print()
#now we display the message 
totalCells=rows*columns
print("-------------ATTENTION----------------")
if((totalCells-1)>toRemove):
    print("A path from the source to the destination is not gurranted")
elif((totalCells-1)<toRemove):
    print("There is at least one path from source to destination")
else:
    print("There is a unique path from source to destination")

DSF=dsf.DisjointSetForest(rows*columns)
totalWalls=toRemove
walls=Lab6.wall_list(rows,columns)
#we begin creating the graph
plt.close("all")
Lab6.draw_maze(walls,rows,columns,cell_nums=True) 
#part from lab 6
while totalWalls!=0:
    d=random.randint(0,len(walls)-1)    
    if Lab6.checkSameSet(DSF,walls[d]) is False:
        Lab6.union_by_size(DSF,walls[d][0],walls[d][1])
        walls.pop(d)
    totalWalls-=1
      
Lab6.draw_maze(walls,rows,columns)
dsf.draw_dsf(DSF)

adjacency_list=to_AList(DSF)
found=breathFS(adjacency_list)
print()
print("Path Found Using Breath First Search:")
print(found)
print()
print("Path Found Using Depth First Search:")
found=depthFS(adjacency_list)
print(found)
print()
print("Path Found Using Depth First Search Recursive")
found=depthFSRecur(adjacency_list)
print(found)
















