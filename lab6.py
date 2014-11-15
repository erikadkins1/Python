# Author: Tyler Baron, Teaching Assistant
# Professor: Richard Whitehouse
# Date: 10/21/2014
# CST 100: Object Oriented Programming Development
# Lab 6
#
# This file is intended as a solution/answer key for this assignment.
#
# NOTE: This was built and tested in Python 2.7
# There are some differences in Turtle between the two versions.
# This means this file will likely have issues in Python 3.x

# Imports
import turtle
import math
import random

# Function Definitions

# Computes the time the projectile takes to reach the given distance.
def calcTime(dist, velo, ang):
    return dist / (velo * math.cos(math.radians(ang)))

# Computes the height of the projectile at the given distance.
def calcHeight(velo, dist, ang):
    time = calcTime(dist, velo, ang)
    return (velo * time * math.sin(math.radians(ang))- ((32.17 * time ** 2)/2))

# Draws the axes and the target to visualize if the projectile hit or not.
def drawStage(dist, tarSize, tarEle, turt):
    # This allows changes made to this variable here to be reflected in the rest of the program.
    global stopXCord
    
    turt.forward(dist)
    stopXCord = turt.xcor()
    turt.left(90)
    turt.pu()
    turt.forward(tarEle)
    turt.pd()
    turt.forward(tarSize)
    turt.pu()
    turt.goto(0, 0)
    turt.pd()
    turt.forward(dist)
    turt.goto(0, 0)
    turt.right(90)

# Will reset the drawing after a shot.
def resetStage(dist, tarSize, tarEle, turt):
    turt.reset()
    turt.pu()
    turt.goto(0, 0)
    turt.pd()
    turt.speed(0)
    drawStage(dist, tarSize, tarEle, turt)
    turt.speed(6)
    turt.left(45)

# Keybind Function Definitions

# Up Arrow Bind: Increase angle of the projectile.
def onUpArrow():
    global angle
    
    angle += 5
    
    # Check boundaries on Angle
    if angle > 85.0:
        angle = 85.0
    else:
        # If we changed the angle, we need to update the turtle's angle.
        tyler.left(5)

# Down Arrow Bind: Decrease the angle of the projectile.
def onDownArrow():
    global angle
    
    angle -= 5

    # Check boundaries on Angle
    if angle < 5.0:
        angle = 5.0
    else:
        tyler.right(5)

# Left Arrow Bind: Decrease the Velocity of the projectile.
def onLeftArrow():
    global velocity
    
    velocity -= 1.0

    # Check that velocity is not 0 or negative.
    if velocity < 1.0:
        velocity = 1.0

# Right Arrow Bind: Increase the Velocity of the projectile.
def onRightArrow():
    global velocity
    
    velocity += 1.0    

# Escape Bind: Quits the program.
def onEscape():
    wn.bye()

# Space Bar Bind: Fires the projectile.
def onSpace():

    # Set up to do calculation incrementally for animation.
    curDistance = 1.0
    height = calcHeight(velocity, curDistance, angle)

    # Main animation loop.
    while (curDistance <= distance) and (height > -1.0):
        tyler.seth(tyler.towards(curDistance, height))
        tyler.setpos(curDistance, height)
        curDistance += 1.0
        height = calcHeight(velocity, curDistance, angle)

# R Key Bind: Resets the stage and turtle.
def onRKey():
    resetStage(distance, size, elevation, tyler)

# Key Values - Set to defaults.
velocity = 100.0
angle = 45.0

# These values are random each run.
distance = random.randint(250, 300)
size = random.randint(1, 10)
elevation = random.randint(2, 50)

# Set up the window, tutle graphic object and draw the problem set up.
wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 350, 350)
tyler = turtle.Turtle()
resetStage(distance, size, elevation, tyler)

# Set up our keybinds.
wn.onkey(onUpArrow, "Up")
wn.onkey(onDownArrow, "Down")
wn.onkey(onLeftArrow, "Left")
wn.onkey(onRightArrow, "Right")
wn.onkey(onEscape, "Escape")
wn.onkey(onSpace, "space")
wn.onkey(onRKey, "r")

# Set the window to listen for events.
wn.listen()
turtle.mainloop()
