
# import re

# patern = r"^[a-z][a-z0-9]\d$"

# while True:
#     username = input("press username or type exit : ")

#     length_username = len(username)
#     print(length_username)
#     if username.lower() == 'exit':
#         break

#     if 5 < length_username <= 10:
#         print("username length valid")
#         x = re.match(patern,username)
#         if x:
#             print("usernmae formate valid")
            
#         else:
#             print("username formate invalid")
#     else:
#         print("username length invalid")


 




## also cehcking length using regex 

import re

patern = r"^[a-z][a-z0-9]{0,8}\d$"

while True:

    username = input("press username or type exit : ")  
    if username.lower() == 'exit':
        break                  
    x = re.match(patern,username)

    if x:
        print("usernmae valid")
            
    else:
        print("username invalid")


   





