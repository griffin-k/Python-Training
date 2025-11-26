#simple function
def greet():
    print("Hello, World!")
greet()

#function with parameters
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("karimullah")


#function with return value
def say_hello(name):
    return f"Hello, {name}!"
print(say_hello("karimullah"))


#function with default parameters
def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

# greet_with_default()
greet_with_default("karimullah")


#function to add two numbers
def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum is: {result}")


#lambda function to greet
greet_lambda = lambda name: f"Hello, {name}!"
print(greet_lambda("karimullah"))


#function as object
def say_bye(name):
    return f"Goodbye, {name}!"
bye = say_bye

print(bye("karimullah"))


#nested function
def outer_function(name):
    def inner_function():
        return f"Hello from the inner function, {name}!"
    return inner_function()
print(outer_function("karimullah"))



#function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("karimullah"))


