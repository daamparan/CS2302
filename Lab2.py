
"""
Author: David Amparan
Course: CS 2302 
Instructor: O. Fuentes 
TA: Anindita Nath, Maliheh Zargaran
Last Modified: 2/25/2019

Purpose: This code is part of a lab assignemnt in which we must implement three types of sorting methods as well as a modified method which
must return the medium without fully sorting the array.
Down below are my codes as well as some of my codes that do not do what I inteded them to do. Functional methods include bubbleSort and quickSort but the
modified quick sort and mergeSort are not functional. 
"""
#creating the class types
import random as rand 

class Node( object ):
    #constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0 #keep track of those added for the getLength

#useful methods for each

"""
Method Name: isEmpty | Parameters: List | Return: Boolean
Functionality: Will take in a list and return whether the list is empty (being
empty at head)
"""        
def isEmpty(L):
    return L.head == None

"""
Method Name: printList | Parameters: L 
Functionality: The method will print all the contents of the list if it is
not empty 
"""
def printList(L):
    temp = L.head #temp to not mess with og List 
   #loop to print all elements
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print() 

"""
Method Name: appendL | Parameters: L, X (item)
Functionality: will append new nodes to the tail of the item
"""
def appendL(L,X):
    if isEmpty(L):
        L.head = Node(X)
        L.tail = L.head
        L.counter +=1
    else:
        L.tail.next = Node(X)
        L.tail = L.tail.next
        L.counter +=1


"""
Method Name: getLength | Parameters: L 
Funtionality: The method attaisns the value of c (in the L object) and 
returns it 
"""
def getLength(L):
    return int(L.counter)




"""
Method Name: Copy | Parameters: L 
Functionality: Creates a copy of the given list and returns it 
"""
def Copy(L):
    if isEmpty(L):
        return L
    
    else: 
        toReturn = List()
        toReturn.head = L.head
        toReturn.tail = L.tail
        toReturn.counter = L.counter
        return toReturn

"""
Method Name: GetELementAt | Parameters: L, index 
Functionality: The method will iterate throgh the list and attain the median of the list, this will be done by taking 
half of the length and finding the number at that position 
"""

def GetElementAt(L, index):
    if isEmpty(L):
        return L
    else:
        counter = 0 #counter will help us go through the list
        temp = L.head
        wanted = 0
        while temp is not None:
            if counter == index:
                wanted = temp.item
            temp = temp.next
            counter += 1
        return wanted

"""
Method Name: Median | Parameters: L 
Functionality: The Median will return a list of the medians found which all come from 
similar sorted lists which were sorted in a different manner
"""
def Median(L, use):
    if isEmpty(L):
        return L
    else: 
        C = Copy(L)
        #sorting method 
        if use == 0:#use bubblesort 
            bubbleSort(C)
            #printList(C)
            #print(getLength(C))
            return GetElementAt(C,getLength(C)//2)
        if use == 1: # use quicksort 
            C = quickSort(C)
            #printList(L)
            #print(getLength(L))
            return GetElementAt(C, getLength(L)//2)
        #if use == 2: # merge sort 
            #L = mergeSort(C)
            #printList(L)
            #print(getLength(L))
            #return GetElementAt(L, getLength(L)//2)
        
        


    
"""
TESTING THE METHODS 
theList = List()
print(getLength(theList))

appendL(theList, 45)
printList(theList)

for i in range(5):
    appendL(theList, i*10)
printList(theList)

print(getLength(theList))
"""

"""
Method Name: Bubble sort Parameters: List 
Functionality: Bubble sort will compare every single item to its 
neighbor and so forth until it reaches the end. A while loop 
with a boolean condition will be used until there are no more 
switches made 
"""
def bubbleSort(L):
    isOrder = False
    changes = 0 #used to count the changes, if one is made then we have not finished
    
    temp = L.head #dont want to mess with the original 
    #have to check incase our lst is empty meaning it is ordered
    if isEmpty(L):
        return
    while isOrder is not True:
        if temp.next is None:##Once we get to the end we want to reset 
            temp = L.head
            changes = 0 
        
        if temp.item > temp.next.item:#comparison and increment in changes
            tempValue = temp.item
            temp.item = temp.next.item
            temp.next.item = tempValue
            changes = 1
        
        temp = temp.next
        
        if temp.next is None and changes == 0:#here we check incase we go through lsit and make no changes
            isOrder = True
"""
Method Name: quickSort | Parameters: L
Functionality: Quick sort is a recursive method that will sort the list
by dividing into two seperate lists with the comparison to a pivot 
then called consecutively until only one item exists and returned 
Finally it will put these two lists together 
"""
def quickSort(L):
    if isEmpty(L):
        return List()
    if getLength(L) <= 1:
        return L
    
    if getLength(L) > 1:
        smallerTP = List()
        biggerTP = List()        
        pivot = L.head.item
        temp = L.head.next
        
        #compare 
        while temp is not None: 
            if pivot > temp.item:
                appendL(smallerTP, temp.item)
            if pivot <= temp.item:
                appendL(biggerTP, temp.item)
            temp = temp.next
        
        #recursive calls 
        smaller = quickSort(smallerTP)
        bigger = quickSort(biggerTP)
        #special conditions that can result 
        #if the list less than piuot is zero then we just the pvot in a list and append it 
       
        test = List()
        if isEmpty(smaller):
            appendL(test, pivot)
            test.head.next = bigger.head
            test.tail = bigger.tail
            return test
        #if the bigger is empty we simply append the pivot
        if isEmpty(bigger):
            appendL(smaller,pivot)
            return smaller
        #similar length so we merge 
        else: 
            appendL(smaller, pivot)
            smaller.tail.next = bigger.head
            smaller.tail = bigger.tail
            return smaller
            
        
"""
Method Name: mergeSort | Parameters: L
Functionality: Divide into two equal pieces and eventually after successfully dividing the list into 
one item which is ordered. After this we put everything back together in order  

"""
def mergeSort(L):
    #base cases
    if getLength(L) == 0:
        return L
    
    if getLength(L) <= 1:
        return L
    #when our list is not just one thing 
    if getLength(L) > 1:
        midpoint = getLength(L)//2
        c = 0
        LH = List()
        RH = List()
        temp = L.head
        
        #here we split 
        while temp is not None:
            if c < midpoint:
                appendL(LH, temp.item)
            #after our midpoint we must insert in Right
            else:
                appendL(RH, temp.item)
            c +=1
            temp = temp.next
        
        #printList(LH)
        #printList(RH)
        
        Left = mergeSort(LH)
        Right = mergeSort(RH)
        n = getLength(Left) + getLength(Right)
        #here we sort the array 
        toReturn = List()
        
        while getLength(toReturn) != n:
            #if our left side is empty 
            if isEmpty(Left):
                appendL(toReturn, Right.head.item)
                Right.head = Right.head.next
            #if our right side is empty 
            if isEmpty(Right):
                appendL(toReturn, Left.head.item)
                Left.head = Left.head.next
            #if neither is none then we must compare and append accordinly 
            if not isEmpty(Left) and not isEmpty(Right):
                if Right.head.item > Left.head.item:
                    appendL(toReturn, Left.head.item)
                    Left.head = Left.head.next
                
                if Right.head.item <= Left.head.item:
                    appendL(toReturn, Right.head.item)
                    Right.head = Right.head.next
        
        return toReturn
        
        
       
"""
Method Name: modifiedQuickSort | Parameters: L, index
Functionality: much like the original quick sort it will sort the list but will get 
rid of one of the extra lists it creates and will return  the list where the median is known to exist
"""
def modifiedQuickSort(L, median):
    if isEmpty(L):
        return List()

    if getLength(L) > 0:
        smallerTP = List()
        biggerTP = List()        
        pivot = L.head.item
        temp = L.head.next
        #we assume the rank of the possible median 
        
        #compare 
        while temp is not None: 
            if pivot > temp.item:
                appendL(smallerTP, temp.item)
            if pivot <= temp.item:
                appendL(biggerTP, temp.item)
            temp = temp.next
        
        #determine where the median is based on the length of the lists 
        if getLength(smallerTP) < median: #n is smaller adn therefore must be within the small list
            median = median - getLength(smallerTP)-1
            return modifiedQuickSort(biggerTP, median)
        
        if getLength(smallerTP) <= median: #if the len of smallerTP is smaller than n, then n cannot be within the small array 
            return modifiedQuickSort(smallerTP, median)
            
        if getLength(smallerTP) == median:
            return pivot
        
        
       
        
        
        
        
test = List()
n = int(input("How many numbers woud you like? "))

for i in range(n):
    appendL(test, rand.randint(0,100))

for i in range(2):
    print("This is the Unsorted List")
    printList(test)
    print("This is the median of that unsorted list")
    print(Median(test,i))






