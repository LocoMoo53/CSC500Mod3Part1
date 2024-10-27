bill = float(input('Enter your the  amount:\n'))
tax = bill * .07
tip = (tax + bill) * .18
total = bill+tax+tip

print('Total for food is ${:.2f}.'.format(bill))
print('Tax at 7% is ${:.2f}.'.format(tax))
print('Tip at 18% is ${:.2f}.'.format(tip))
print('Total for everything is ${:.2f}.'.format(total))
