'''
 A different store has a lower price where the final price the consumer pays for the soda is only $8.00.
 The consumer has $50 and wants to buy as many cases of soda as they can(they cannot buy partial cases). 
 What is their change? Hint: use the mod function.
'''
case = 8
money_available = 50

change = case % money_available
print("Your change is: $", change)

'''
    >>> exec(open('challenge2.py').read())
    Your change is: $ 8
'''
