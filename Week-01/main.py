

# from Package import bye_module
# bye_module.saybye()



# from Package import math_module

from Package.math_module import *



number1 = float(input("Enter the 1st no : "))
number2 = float(input("Enter the 2nd no : "))

print("Select operation:")
print("1 addition ")
print("2 subtraction")
print("3 multiplication")

operation = int(input("select the operation 1 - 2 - 3 : "))

if operation == 1 :
    # result = math_module.add(number1,number2)
    result = add(number1,number2)
    print(f"the addition of the numbers you entered is {result}")

elif  operation==2:
    result =  sub(number1,number2)
    print(f"the subtraction of the numbers you entered is {result}")

elif  operation==4:
    result = multiply(number1,number2)
    print(f"the multiplication of the numbers you entered is {result}")

else:
    print("Select the available options")




