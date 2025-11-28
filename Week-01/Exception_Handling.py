





# try :
#     print(a)
# except:
#     print("variable is not defined")



# try:
#   print("Hello")
# except:
#   print("someting went wrong")
# else:
#   print("try execute without error")




# def addition(x, y):
#     try:
#         result = x + y
#         return result
#     except TypeError:
#         return "provide int only "
#     except Exception as e:
#         return f"An error occurred: {e}"

    

# print(addition(5, "10"))



# try:
#     file = open("karimullah.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Execution completed.")   



# try:
#     file = open("karimullah.txt", "w")
#     content = file.read("hello")
# except Exception as e:
#     print(e)
# finally:
#     print("Execution completed.")   





# number= int(input("enter the no btw 2-9 : "))

# if 2 < number <= 9 :
#     print("you enter the correct number") 

# else :
#     raise Exception("you entered the invalid number number must be btw 2-9")