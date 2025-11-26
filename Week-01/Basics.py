
# Variables & Data Types

#type casting
age = "20"     
age = int(age) 


#checking if number is integer
data = input("Enter something: ")

if data.isdigit():
    print("You entered a number")
else:
    print("This is not a number.")


#Swapping variables
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)



#default input value
name = input("Enter name (default=Guest): ") or "Guest"
print(name)


# Escape Sequences
print("Hello \n World")     
print("He said \"Hello\"") 
print("Path: C:\\Users\\Karim")


#using seprate functions to print
print("Karim", "ullah", sep="-")
print("Karim", "ullah", sep="\n")


#multiple assignments
x, y, z = 10, 20, 30
print(x, y, z)



age = 20 
name ="karimullah"
height ="5.7"
is_student = True
print(type(age))
print(type(name))
print(type(height))
print(type(is_student))


##print using simple , 
print("My name is", name, "I am", age, "years old and my height is", height, "and I am a student")
##print using contactination 
print("My name is " + name + " I am " + str(age) + " years old and my height is " + str(height) + " and I am a student")
##print using f string
print(f"My name is {name} I am {age} years old and my height is {height} and I am a student")




#User Input / Output
name = input("enter you name => ")
card  = input("enter your card No => ")
print(f"Hello {name} welcome back. your card No is {card} ")


# Multiple Inputs in One Line
name , card =input("Please Enter your Name and Card No :  ").split()
print(f"Hello your name is: {name} , and you card No is : {card} ") 


# To get the hidden input 
import getpass
card =getpass.getpass("please enter your card No :")
print(f"your card no is : {card}")


