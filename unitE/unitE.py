from turtle import *

screen1 = Screen()
t = Turtle()
t.shape("turtle")
t.pensize(3) # line width

# right side of the car 
t.color("ForestGreen")
t.fd(100) # first half of the top's length
t.rt(90) 
t.fd(100) # down from top to trunk
t.lt(90)
t.fd(100) # trunk
t.rt(90)
t.fd(100) 
t.rt(90)
t.fd(50)
# back tire
t.color("Black") 
t.rt(90)
t.circle(50)
t.lt(90)
t.pu()
t.fd(100)
t.pd()
# car's bottom
t.color("ForestGreen")
t.fd(100)
# front tier
t.color("Black")
t.rt(90)
t.circle(50)
t.lt(90)
t.pu()
t.fd(100)
t.pd()
# left side of the car
t.color("forestGreen")
t.fd(50)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(100)

# first ballon
t.pu()
t.fd(100)
t.lt(90)
t.fd(150)
t.pd()
t.color("Black")
t.fd(85)
t.rt(90)
t.color("Blue")
t.fillcolor("Magenta")
t.begin_fill()
t.circle(50)
t.end_fill()

# second ballon
t.lt(180)
t.pu()
t.fd(350)
t.pd()
t.color("Blue")
t.fillcolor("Magenta")
t.begin_fill()
t.circle(50)
t.end_fill()
t.lt(90)
t.pu()
t.fd(100)
t.pd()
t.color("Black")
t.fd(85)
t.pu()

t.home()
print(t)
