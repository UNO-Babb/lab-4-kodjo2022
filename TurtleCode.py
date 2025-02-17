#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(myGon, sides):
    for s in range(sides):
        myGon.forward(50)
        myGon.right(360/sides)
        
def fillCorner (bob, corner):
    # draw big square
    drawSquare(bob, 100)
    if corner ==1:
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()
    elif corner == 2:
        bob.forward(50)
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()
           
def squaresInSquares(myTurtle, n, size=20, increment=20):
    for i in range(n):
        myTurtle.penup()
        myTurtle.goto(-size/2, size/2)  
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size += increment  

def main():
    myTurtle = turtle.Turtle()
    
    drawSquare(myTurtle, 100) 
    drawPolygon(myTurtle, 5) #draws a pentagon 
    drawPolygon(myTurtle, 8) #draws an octogon 
    
    
    fillCorner(myTurtle, 1) 
    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
