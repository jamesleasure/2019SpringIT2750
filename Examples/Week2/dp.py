def drawPolygon(myTurtle,sideLength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)
        
# example usage
# from dp import *
# import turtle
# t = turtle.Turtle()
# drawPolygon(t, 10, 10)
