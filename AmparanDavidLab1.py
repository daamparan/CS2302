
"""
Author: David Amparan
CS 2302 
Last Date Modified: February 8, 2019 
Instructor: O.Fuentes 
Assingment: Lab 1
TA: Anindita Nath & Maliheh Zaragan
Purpose: This code will serve as practice for recursion as well as an introduction to the 
benefits of python, various geometric shapes will be drawn and each method will be ran 3 times creating 3 different outputs
to show the full functionality of them
"""
import numpy as np
import matplotlib.pyplot as graph
import math

"""
Method Name: draw circle | Parameters: ax, n, center, radius, w
Functionality: This is the method that Professor Fuentes provided except with five recursive calls to 
succesfully draw the last difure requested. This is done by attaining the ratio of the radius divided 3 times the correct 
weight 
"""
def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        #first call for middle circle 
        draw_circles(ax,n-1,center,radius//3,w)
        #x is the ratio of the radius divided by 3 since you want three circles 
        x = radius/3
        #depending on which you want you either add the ratio or subtract 
        draw_circles(ax, n-1,[(center[0]-(x*w)), center[1]], radius//3, w )
        draw_circles(ax, n-1, [(center[0]+(x*w)), center[1]], radius//3, w)
        draw_circles(ax, n-1, [center[0], (center[1]-(x*w))], radius//3, w)
        draw_circles(ax, n-1, [center[0], (center[1] + (x*w))], radius//3, w)


"""
Method Name: attainKids| Parameters (root, height, length)
Functionality: will pass the root and produce the daughter cells of these,
The daughter roots will be based on half of the length and 50% of the remaning height
"""
def attainKids(root, height, length):
    #here we will give the coordinates for the left and right children
    left, right = np.zeros((2,2))
    left[0] = root[0]-(length//2)
    right[0] = root[0]+(length//2)  #Here all we do is take half of the given measurments and either add or sub
    left[1] = root[1] - (height*.50)
    right[1] = root[1]-(height*.50)
    return left, root, right 
    
"""
Method Name: binary_tree | Parameters: ax, height, root, length, toMulti
Functionality: Binary tree will take in the ax to draw onto as well as the height, root, and length 
to impliment on attainKids and plot the returned points 
"""  
def binary_tree(ax, height, root, length, toMulti):
    if height>0:
        #i attain the coordinates for the daughter cells then put them in arrau
        left_right = attainKids(root, toMulti, length)
        coor = np.zeros((3,2))
        #convert to array to avoid any error when slicing to plot
        for i in range(3):
            coor[i] = left_right[i]
            
        ax.plot(coor[:,0], coor[:,1], color = 'k')
        ax.plot()
        #recursive call
        binary_tree(ax, height//2, coor[0], length//2, toMulti)
        binary_tree(ax, height//2, coor[2], length//2, toMulti)


"""
Method Name: the_hole | Parameters:ax,n,center,radius,width|
Functionality: This method will take in the paramets which will be used for the 
composition of a circle figure, then will be ploted. THIS METHOD ALSO INTEGRATES PARTS 
OF THE SHARED CODE BY PROFESSOR FUENTES 
"""
def the_hole(ax,n,center,radius, weight):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        #here we modify the center as we begin to push left
        center[0] = center[0]*weight
        #recursive call
        the_hole(ax, n-1, center, radius*weight, weight)
"""
Method Name: circle | Parameters: center, radius| Returns an xy array 
Functionality: circle will calculate the circles circumference 
and create a set of points for that circumeference 
"""
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0, 6.3, n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y


"""
Method Name: the_squares | Parameters: axis, times it will iterate, the origin, length of side
Functionality: The method will draw the squares, these will be ploted
by the pairs from the 2D array. The radius parameter also indicates the size 
for the consecutive corner squares which will also use a center 
"""
def the_squares(ax,n,origin,length):
    if n>=0:
        #call method to attain coordinates an begin plotting 
        p = pointsSquare(origin,length)
        #by adding the for loop we allow the coordinates to become an array not a tuple
        coor = np.zeros((5,2))
        for i in range(len(p)):
            coor[i] = p[i]
    
        #iterator = [1,2,3,0,1]
        ax.plot(coor[:,0],coor[:,1], color='k')
        ax.plot()
        #RECURSIVE CALL
        the_squares(ax,n-1, coor[0], length//2)
        the_squares(ax,n-1, coor[1], length//2)
        the_squares(ax,n-1, coor[2], length//2)
        the_squares(ax,n-1, coor[3], length//2)
""""
Method Name: pointsSquare | Parameters: center, length | Return Type: Pairs
Center squares will return the points for the corresponding origin. It will use the length
to give the correct points to attain a symmetrical square   
"""  
def pointsSquare(center,length):
    #here we reduce the size to get even points
    radius  = length//2
    #the top left and bottom right coordinates have to modified carefully since they involve 
    #the oppostie operation for each element in the center array 
    
    x=center[0] #x and y must be created to help with the pass by reference issue, thus we create new array
    y=center[1]
    topLeft = np.array([x-radius,y+radius])
    bottomRight = np.array([x+radius, y-radius])
    
    #once we return we have the coordiantes for the correspinding center       
    return center-radius, topLeft, center+radius, bottomRight, center-radius 

#adding the for loop allows us to repeat the demonstration three times 
squares = 1
for i in range(3):
    length = 100 
    origin = np.array([0,0])
    #graph.close("all")
    fig, ax = graph.subplots()
    the_squares(ax, squares, origin, length)
    ax.set_aspect(1.0)
    ax.axis("off")
    graph.show()
    #fig.savefig('squares.png')
    squares+=1

#loop for the circles
totalC = [10, 50, 100]
radi = [.6, .9, .95]

circles = 1
for i in range(3):
    #graph.close("all")
    fig, ax = graph.subplots()
    the_hole(ax, totalC[i], [100,0], 100, radi[i])
    ax.set_aspect(1.0)
    #ax.axis('off')
    graph.show()
    #fig.savefig('circles.png')
    
#loop for the binary tree
#variables to change values
heights = [4, 10, 40]
for i in range(3):
    #graph.close("all")
    fig, ax = graph.subplots()
    binary_tree(ax, heights[i], [0,100], 100, 100)
    ax.set_aspect(1.0)
    #ax.axis("off")
    graph.show()
    #fig.savefig('circles.png')
#for loop for the draw circles
tripCircles = [3,4,5]
for i in range(3):
    #graph.close("all")
    fig, ax = graph.subplots()
    draw_circles(ax, tripCircles[i], [100,100], 100, 1.95)
    ax.set_aspect(1.0)
    ax.axis("off")
    graph.show()
    #fig.savefig('tripCircles.png')
    
    
    