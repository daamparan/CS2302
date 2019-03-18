"""
Author: David Amparan
Last Modified: 3/17/2019
TA: Anindita Nath, Malileh Zaragan
Professor: Fuentes, Olac 
Functionality: Implement the functionalities of a B-Tree as well 
as learn the implementation and different modes of traversal 

"""
class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   

def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
"""
Method Name: compHeight Parameters: T 
Functinality: It will compute the height of the tree and return that number 
"""
def compHeight(T):
    if T.isLeaf:
        return 0
    return compHeight(T.child[0])+1


"""
Method Name: intoSortlist | Parameters: B Tree
Funtionalty: For this method we will traverse the B-Tree and 
extract the items in a sorted manner and store them within a list 
"""
        
def intoSortList(T):
    if T.isLeaf:
        return T.item
    #after returning the keafs we must concatanate the root to the other parts 
    ourList = []
    givenBack = []
    #here we append the left side then root then the next and so on so forth
    for i in range(len(T.item)):
        givenBack = intoSortList(T.child[i])
        ourList = ourList + givenBack
        ourList = ourList + [T.item[i]]
    #this recursive call is to traverse the right side of our B Tree
    ourList = ourList + intoSortList(T.child[len(T.item)])
    return ourList

"""
Method Name: minDepth | Parameters: BTree and Depth
Functionality: Given a BTree find the mininum element at that given depth
"""
def minDepth(T, d):
    if d==0:
        return T.item[0]
    #if d is not zero and we are at a leaf then the depth exceeds the height of the tree
    if T.isLeaf:
        return -1
    return minDepth(T.child[0], d-1)


"""
Method Name: maxDepth | Parameters: B Tree, Depth
Parameters: Similar to the minDepth method we will find the max element 
at a given depth
"""
def maxDepth(T,d):
    if d==0:
        return T.item[-1]
    if T.isLeaf:
        return -1
    return maxDepth(T.child[-1],d-1)


"""
Method Name: nodesAtDepth(T,d) | Parameters: BTree and Depth 
Functionality: We will return the number of nodes at that given depth and if the
depth is not found then we will return -1
"""
def nodesAtDepth(T,d):
    if d==0:
        return 1
    if T.isLeaf:
        return 0
    nodes = 0
    for i in range(len(T.item)):
        nodes = nodes + nodesAtDepth(T.child[i], d-1)
    nodes = nodes + nodesAtDepth(T.child[len(T.item)],d-1)
    return nodes
    

"""
Method Name: printDepth | Parameters: T, D 
Functionality: The method will traverse through a given depth
and if it exists, it will print all items at that depth
"""
def printDepth(T, d):
    if d==0:
        for i in T.item:
            print(i,',',end=' ')
    if T.isLeaf:
        return
    #to traverse both sides of the tree require a forloop 
    for i in range(len(T.item)):
        printDepth(T.child[i],d-1)
    printDepth(T.child[len(T.item)], d-1)


"""
Method Name: fullNodes | Parameters: T
Functionality: fullNodes will traverse the entire tree and 
determine which nodes are full, if the nodes are full then we will return 1
Will count all full nodes in the tree
"""
def fullNodes(T):
    #initial comparison
    if T.isLeaf:
        if len(T.item)==5:
            return 1
        else:
            return 0
    if len(T.item)==5:
        return 1
    
    #recursive calls to traverse left side and right side
    total = 0
    for i in range(len(T.item)):
        total = total + fullNodes(T.child[i])
    total = total + fullNodes(T.child[len(T.item)])
    return total

"""
Method Name: fullLeaves | Parameters: B Tree
FUnctionality: Will count the amount of full leaves and return that number 
"""
def fullLeaves(T):
    #we only care about the leaves
    if T.isLeaf:
        if len(T.item)==5:
            return 1
        else:
            return 0
    total = 0
    for i in range(len(T.item)):
        total = total + fullLeaves(T.child[i])
    total = total + fullLeaves(T.child[len(T.item)])
    return total

"""
Method Name: depthOfK | Parameters: T, k, d
Functionality: The method will run through the entire tree while keeping
tabs on the depth traveled to return that depth if the item is found 
"""
def depthOfK(T,k,d):
    #if we end up at a leaf we check if it is within 
    if T.isLeaf:
        if k in T.item:
            return d
        else:
            return -1
    #now we check incase it is within a seperate node 
    if k in T.item:
        return d
    
    #recursive call 
    return depthOfK(T.child[FindChild(T,k)], k, d+1)
    
    
    
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
#L = [30, 50, 10, 20, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()

for i in L:
    Insert(T,i)
    
    
print("Our B-Tree")
PrintD(T, '')
print("--------------------------------------")
print("Computing Height of the Tree")
print("Height:", compHeight(T))
print()
print("--------------------------------------")
print()
print("Sorted List from the Tree")
print("List:", intoSortList(T))
print()
print("--------------------------------------")
print()
d = 1
print("Minimum value at depth", d)
print("Minimum at depth", d,":", minDepth(T,d))
print()
print("--------------------------------------")
print()
print("Maximum value at depth", d)
print("Maximum at depth", d,":", maxDepth(T,d))
print()
print("--------------------------------------")
print()
print("Total number of Nodes at a Depth")
print("Nodes at depth", d, ":", nodesAtDepth(T,d))
print()
print("--------------------------------------")
print()
print("Printing the elements of certain depth")
printDepth(T,d)
print()
print("--------------------------------------")
print()
print("The number full Nodes")
print("Full Nodes:", fullNodes(T))
print()
print("--------------------------------------")
print()
print("Number of full Leaves")
print("Full Leaves", fullLeaves(T))
print()
print("--------------------------------------")
print()
print("The Depth of an item present in the B-Tree")
k = 50
d = 0
print("Searching for", k, ", depth:", depthOfK(T,k,d))
        
        
        
        
        
        
        
        
        




