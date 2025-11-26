print("Day-01 Welcome to Simple Calculator!")

number1 = float(input("Enter the First NO : "))
number2 = float(input("Enter the First NO : "))

print("Select operation:")
print("1 Addition (+)")
print("2 Subtraction (-)")
print("3 Multiplication (*)")

operation = int(input("select the operation 1 - 2 - 3 : "))

if operation == 1 :
    result = number1+number2
    print(f"the Addition of the numbers you entered is {result}")

elif  operation==2:
    result = number1 - number2
    print(f"the Subtraction of the numbers you entered is {result}")

elif  operation==4:
    result = number1 * number2
    print(f"the Multiplication of the numbers you entered is {result}")

else:
    print("Select the available options")


