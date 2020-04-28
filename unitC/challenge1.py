'''
Assignment:
      A store charges $10.00 for a case of soda (24 cans).
      They are having a 20% off sale, but the consumer must pay tax of 10% 
      and a can deposit of $.05 per can (there is no tax or discount on this
      deposit charge). Calculate and display the final price the consumer pays for the soda.
'''
case = 24
price = 10
sale = 20
tax = 10
deposit = .05

sale_price = price - (price * sale / 100)
print("Invoice\n")
print("Price with %20 off: $",sale_price)
tax_total = (sale_price * 10 / 100)
print("Purchase tax(%10): $", tax_total)
deposit_total = (case * deposit)
print("Can deposit($0.05): $ %.1f" % deposit_total)
total = sale_price + tax_total + deposit_total
print("------------------------")
print("Total price: $", total)

'''
    >>> exec(open('challenge1.py').read())
    Invoice

    Price with %20 off: $ 8.0
    Purchase tax(%10): $ 0.8
    Can deposit($0.05): $ 1.2
    ------------------------
    Total price: $ 10.0
'''
