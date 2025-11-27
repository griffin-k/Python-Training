##simple file write
# file = open('info.txt','w')
# content = file.write("Hello how are you")


##simple file read
# file = open('info.txt','r')
# content= file.read()
# print(content)


#file write in append mode
# file = open('info.txt','a')
# content = file.write("\nhey i am doing well")
# file.close()


#close file 
# file = open('info.txt','r')
# content= file.read()
# print(content)
# file.close()


#close file with statment
# with open('info.txt','r') as file :
#      content = file.read()
#      print(content)



# with open('info.txt','r') as data :
#     content =data.read() 
#     print(len(content))


# with open('info.txt','r') as data :
#     content =data.readlines() 
#     print(len(content))




# with open('info.txt','r') as data:
#     content= data.read()
#     result = content.split(' ')
#     print(result)
#     print(len(result))



#count specific data in file

# with open('info.txt','r') as file :
#     content = file.read()
    
# a , d , s ,sc = 0,0,0,0

# for ch in content :
#     if ch.isalpha():
#         a += 1
#     elif ch.isdigit():
#         d += 1
#     elif ch.isspace():
#         s += 1
#     else :
#         sc += 1 

# print(f"alphabate {a}")
# print(f"digit {d}")
# print(f"space {s}")
# print(f"special chr  {sc}")




# #count specific data in each line

# with open('info.txt','r') as file: 
#     content = file.readlines()

# # a,  d, s ,sc = 0,0,0,0

# for line in content:
#     a,  d, s ,sc = 0,0,0,0
#     for ch in line:
#         if ch.isalpha():
#             a += 1
#         elif ch.isdigit():
#             d += 1
#         elif ch.isspace():
#             s += 1
#         else :
#             sc += 1


#     print("\n")
#     print(line)
#     print("\n")
#     print(f"alphabate {a}")
#     print(f"digit {d}")
#     print(f"space {s}")
#     print(f"special chr  {sc}")
#     print("\n")


    

# ## check vowels

# with open('info.txt','r') as file:
#     content = file.read()

# v,c = 0,0

# for ch in content :
#     if ch in ['a','e','i','o','u'] :
#         v +=1 
#     elif ch.isalpha():
#         c +=1 

# print(v,c)






#check specific char 
# with open('info.txt','r') as file:
#     content=file.readlines()

# print(content)
# k = 0 
# for list in content:
#     if 'k' in list:
#         k += 1
#     else :
#         print(" k not found")

# print(f"the k in presnt {k} times")



# with open('info.txt', 'r') as file:
#     content = file.read()

# count_k = content.count('k')

# print(f"'k' presnt {count_k} times")




##write multiple lines 
# with open('info.txt', 'w') as file:
#     content=file.writelines(['hello my name is karimullah\n','i am from lhr\n','here we go\n'])





# #copy data frm file a to b 
# data =open('file_a.txt','r')
# datab = open('file_b.txt','w') 
# content=data.read()
# content=datab.write(content)
# data.close()
# datab.close()



# #file from diff location
# with open(r'File Handling/index.txt','w+') as file :
#      username = input("Plx enter your name : ")
#      user = file.write(username)

      


# read and write using user input 
index_path = r'File Handling/index.txt'

with open(index_path,'r+') as file:
    content = file.read()
    print(content)
    username = input("plx enter your name : ")
    data = username.capitalize()
    file.write("\n" + data)
    file.seek(0)
    print(file.read())











     