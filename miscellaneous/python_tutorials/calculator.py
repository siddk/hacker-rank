"""
calculator.py

Add, subtract, multiply, divide, and integer divide two numbers
"""

number1 = float(raw_input())
number2 = float(raw_input())

#addition
add = number1 + number2
print "%.2f" % (add)

#subtraction
sub = number1 - number2
print "%.2f" % (sub)

#multiplication
mul = number1 * number2
print "%.2f" % (mul)

#division
div = number1 / number2
print "%.2f" % (div)

#integer division
ind = number1 // number2
print "%.2f" % (ind)
#print "%.2f" % record_dict[target]
