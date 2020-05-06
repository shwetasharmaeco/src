from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce
def calculator():
    while True:
        try:
            print("\n\n")
            print(" Choose from following functions:\n +: addition\n - :subtraction\n *: multiply\n /: divide\n square: square of the number\n cube: cube of the number\n pow: first number to the power of second number\n mod: remainder after dividing first number by second number\n press q to quit" )
            input_string=input( "please type operator followed by space and numbers >")

            tokens= input_string.split()

            if "q" in tokens:
                break

            operator, *nums = tokens

            nums_lst=[]
            for num in nums:
                nums_lst.append(float(num))

        except:
            print("Only numbers allowed")
            continue

        if operator not in ["square", "cube"] and len(nums_lst)<2:
            print("not enough numbers provided")
            continue
        if operator in ["square", "cube"] and len(nums_lst)!=1:
            print (f"Only one number allowed to run {operator}")
            continue

        result = None

        if operator=="+":
            result= (reduce(add,nums_lst))

        elif operator == '-':
            result = reduce(subtract, nums_lst)

        elif operator == '*':
            result = reduce(multiply, nums_lst)

        elif operator == '/':
            result = reduce(divide, nums_lst)

        elif operator == 'square':
            result = square(nums_lst[0])

        elif operator == 'cube':
            result = cube(nums_lst[0])

        elif operator == 'pow':
            result = reduce(power, nums_lst)

        elif operator == 'mod':
            result = reduce(mod, nums_lst)

        else:
            print ("Wrong operator entered")
            continue

        print(result)
            

calculator()


