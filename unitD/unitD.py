# 1. Request the user's name and welcome the user.
def welcome():
  name = input("Welcome, friend. Please enter your name: ")
  print("Hello, {}".format(name))

welcome()

# 2. Print the area of a square
def printSquareArea(side):
  area = side * 4
  print("Area of the square with a side of {} = {}".format(side, area))

printSquareArea(3)

# 3. Print the area of a rectangle
def calcRectangleArea(length, width):
  area = length * width
  return area

rectangleArea = calcRectangleArea(4,5)
print("Area of a rectangle with a length of 4 and a width of 5 = {}".format(rectangleArea))

# 4. Print the volume of a box, where each side is a rectangle.
def printRectangleVolume(length, width, heigth):
  area = calcRectangleArea(length, width)
  volume = area * heigth
  print("Volume of a rectangle with a length of 4, width of 5 and a height of 6 = {}".format(volume)) 

printRectangleVolume(4,5,6)

'''

Welcome, friend. Please enter your name: Rimma
Hello, Rimma
Area of the square with a side of 3 = 12
Area of a rectangle with a length of 4 and a width of 5 = 20
Volume of a rectangle with a length of 4, width of 5 and a height of 6 = 120

'''
