"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if len(tokens) == 1:
        operator = tokens[0] 
    elif len(tokens) == 2:
        operator, num1 = tokens
        num1 = int(num1)
    elif len(tokens) == 3:
        operator, num1, num2 = tokens
        num1 = int(num1)
        num2 = int(num2)

    if operator == '+' and len(tokens) == 3:
        print add(num1, num2)

    elif operator == '-' and len(tokens) == 3:
        print subtract(num1, num2)

    elif operator == '*' and len(tokens) == 3:
        print multiply(num1, num2)

    elif operator == '/' and len(tokens) == 3:
        print divide(num1, num2)

    elif operator == 'square' and len(tokens) == 2:
        print square(num1)

    elif operator == 'cube' and len(tokens) == 2:
        print cube(num1)

    elif operator == 'pow' and len(tokens) == 3:
        print power(num1, num2)

    elif operator == 'mod' and len(tokens) == 3:
        print mod(num1, num2)

    elif operator == 'q' and len(tokens) == 1:
        break

    else:
        print "I didn't understand your input."