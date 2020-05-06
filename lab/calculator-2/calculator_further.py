from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )



while True:
    
    print(" Choose from following functions:\n +: addition\n - : subtraction\n *: multiply\n /: divide\n sq: square of the number\n cube: cube of the number\n pow: first number to the power of second number\n mod: remainder after dividing first number by second number"   )
    input_string = (input (" type your func code and number(s) with a space \n or press q to quit >"))

    tokens = input_string.split()

    

    if "q" in tokens :
        break



    operator, *nums = tokens

    #only numbers allowed
    nums_lst=[]
    try:
        for num in nums:
            nums_lst.append(float(num))
    except:
        print("Only numbers allowed to perform a function")
        continue

    #correct amount of numbers provided
    if operator not in ["sq","cube"] and len(nums_lst)<2:
        print("not enough numbers entered")
        continue

    

    result= None

    num1=tokens[1]
    num2=tokens[2]

    if operator=="+":
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

    else:
        print("Invalid operator entered")
        continue

    print (result)