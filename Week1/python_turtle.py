# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 175
for x in range(0,7):
    print "x", x
    for y in range(1,6):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.left(75)
        # advance according to set distance
        turtle.forward(DIST)
        turtle.backward(DIST)
    # add to set distance
    DIST += 10
###TWEAKED IT A LITTLE BIT AND MADE A STAR!!!