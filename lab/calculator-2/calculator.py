"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def build_cal2():
    while True:
        print(" Choose from following functions:\n +: addition\n - : subtraction\n *: multiply\n /: divide\n sq: square of the number\n cube: cube of the number\n pow: first number to the power of second number\n mod: remainder after dividing first number by second number"   )
        input_string = input (" type your func code and number(s) with a space \n or press q to quit >")

        tokens = input_string.split()
        operator=tokens[0]
        num1=float(tokens[1])
        num2=float(tokens[2])
        

        result=None
    
        if operator=="q" :
            break

        elif operator=="+":
            result = add(num1, num2)

        elif operator=="-":
            result = subtract(num1, num2)

        elif operator=="*":
            result = multiply(num1, num2)

        elif operator=="/":
            result = divide(num1, num2)

        elif operator=="sq":
            result = square(num1)

        elif operator=="cube":
            result = cube(num1)

        elif operator=="pow":
            result = power(num1, num2)

        elif operator=="mod":
            result = mod(num1, num2)

        print (result)


build_cal2()


