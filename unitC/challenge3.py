'''
 How many cases of soda can the consumer buy?
'''
# import math module to access math.floor function
import math
case = 8
money_available = 50

total_cases = math.floor(money_available / case)
print("Soda cases total: ", total_cases)

'''
    >>> exec(open('challenge3.py').read())
    Soda cases total:  6
'''
