# Part 1. Display the user's name
yourName = input("Welcome, human! Please enter your name: ")
print("Hello there,", yourName)

# Part 2. Data types
whatAmI = 10
print("\n")
print("whatAmI type for '10' is: ", type(whatAmI))
whatAmI = 1.5
print("whatAmI type for '1.5' is: ", type(whatAmI))
whatAmI = "Hi"
print("whatAmI type for 'Hi' is: ", type(whatAmI))

# Part 3. Numbers
print("\n")
num1 = int(input("Now, please enter a number: "))
num2 = int(input("Please enter another number: "))

print("\n")
# substruct numbers
res = num1 - num2
print('{} - {} = {}'.format(num1, num2, res))
# divide numbers
res = num2 / num1
print('{} / {} = {}'.format(num1, num2, res))
# multiply numbers
res = num1 * num2 ** num2
print('{} * {} ** {} = {}'.format(num1, num2, num2, res))
# module
res = num1 % num2
print('{} % {} = {}'.format(num1, num2, res))
print("Thanks for using my program. Live long and prosper.")

'''
Execution results: 
    Welcome, human! Please enter your name: General Kenobi
    Hello there, General Kenobi


    whatAmI type for '10' is:  <class 'int'>
    whatAmI type for '1.5' is:  <class 'float'>
    whatAmI type for 'Hi' is:  <class 'str'>


    Now, please enter a number: 5
    Please enter another number: 3


    5 - 3 = 2
    5 / 3 = 0.6
    5 * 3 ** 3 = 135
    5 % 3 = 2
    Thanks for using my program. Live long and prosper.
'''
