from turtle import *

s = Screen()
t = Turtle()
t.hideturtle()
t.pu()
t.pensize(70)
t.speed(0)

# initial params
size = 70
upperLeftX = -350
upperLeftY = 300
start = (upperLeftX, upperLeftY)
t.goto(start)

# draw 1 square
def  drawSquare(x, y, color):
    t.goto(x, y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range (4):
        t.fd(size)
        t.rt(90)
    t.end_fill()
 
# complete 1 row
column = 1
while (column <= 8):
    upperLeftX+=size
    
    if (column % 2 == 0):
        color = "red"
    else:
        color = "black"
        
    drawSquare(upperLeftX, upperLeftY, color)
    column+=1
    

