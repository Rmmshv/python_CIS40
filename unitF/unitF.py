from turtle import *
import random

screen1 = Screen()
t = Turtle()
t.shape("triangle")
t.hideturtle()

# draw a circle
def drawCircle(r, color):
    t.home()
    t.color(color)
    t.pu()
    t.rt(90)
    t.fd(r)
    t.pd()
    t.lt(90)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.home()
# draw the target
drawCircle(300, 'blue')
drawCircle(200, 'red')
drawCircle(100, 'yellow')

# setting initial values
aScore = 0
bScore = 0
aMinDist = 300
bMinDist = 300
aColor = "#00FF00" # #00FF00 - Hex code for lime color
bColor = "#C0C0C0" # #C0C0C0 - Hex code for silver color

# generate a random distance and angle on the circle
def  arrowShot(c):
    t.pu()
    t.home()
    t.color(c)
    dist = random.randint(0,300)
    h = t.setheading(random.randint(0,359))
    t.fd(dist)
    t.setheading(90)
    t.pd()
    t.stamp()
    return dist
# get the score for each shot
def getScore(dist):
    if (dist >=0 and dist <= 100):
        score = 10
    if (dist >= 101 and dist <= 200):
        score = 7
    if (dist >= 201 and dist <= 300):
        score = 5
    return score

# Archer A's 3 shots
dist = arrowShot(aColor)
aScore = getScore(dist)
a1 = aScore

dist = arrowShot(aColor)
aScore = getScore(dist)
a2 = aScore

dist = arrowShot(aColor)
aScore = getScore(dist)
a3 = aScore
# Archer A's total score
sumA = a1+a2+a3

# Archer B's 3 shots
dist = arrowShot(bColor)
bScore = getScore(dist)
b1 = bScore

dist = arrowShot(bColor)
bScore = getScore(dist)
b2 = bScore

dist = arrowShot(bColor)
bScore = getScore(dist)
b3 = bScore
# Archer B's total score
sumB = b1+b2+b3

# find and print the result of the match
if (sumA > sumB):
    print("Archer A is a winner. Score: {}".format(sumA))
if (sumA < sumB):
    print("Archer B is a winner. Score: {}".format(sumB))
if (sumA == sumB):
    print("It's a tie! Archer A's score: {}, Archer B's score: {}".format(sumA, sumB))

