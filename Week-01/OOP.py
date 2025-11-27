# simple class

# class Student:
#     def __init__(self,name,grade):
#         self.name= name
#         self.grade =grade

# student1 =Student("karimulllah",12)
# print(student1.name)
# print(student1.grade)



# class with methord

# class Student:
#     def __init__(self,name,grade):
#         self.name= name
#         self.grade =grade

#     def Student_result(self):
#         print(f"student name is {self.name},is in {self.grade}")

# student1 =Student("karimulllah",12)
# # student1.Student_result()
# print(student1.__dict__)


# modify obj properties

# class Student:
#     def __init__(self,name,grade,percentage,team):
#         self.name= name
#         self.grade =grade
#         self.percentage=percentage
#         self.team =team

#     def Student_result(self):
#         print(f"student name is {self.name},is in {self.grade} with {self.percentage} percentage")



# team1 = "Jinha"
# team2 = "Iqbal"

# student1 =Student("karimulllah",12,80,team1)
# student1.Student_result()
# print(student1.__dict__)

# print(student1.percentage)
# student1.percentage=60
# print(student1.percentage)
# del student1.percentage
# print(student1.__dict__)




# encapsulation
###################

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name= name
#         self.grade =grade
#         self.__percentage=percentage

#     def get_percentage(self): 
#         return self.__percentage

# student1=Student("karimullah",12,80)

# print(student1.get_percentage())



# inheritence 
###################

#parent class 
# class Student:
#     def __init__(self,name,grade):
#         self.name= name
#         self.grade =grade

# student1=Student("karimullah",12)


# #child class
# class Passout_Students(Student):
#     def __init__(self, name, grade,campus):
#         super().__init__(name, grade)
#         self.campus=campus


# gradu_student=Passout_Students("karimullah",12, "main")
# print(gradu_student.__dict__)





#polymorphism
###################

# Parent class
class Student:
    def __init__(self,name,grade):
        self.name= name
        self.grade =grade


    def get_data(self):
        print(f"student name is{self.name} in {self.grade} grade")


student1=Student("karimullah",12)

# child class
class Passout_Students(Student):
    def __init__(self, name, grade,campus):
        super().__init__(name, grade)
        self.campus=campus


    def get_data(self):
        print(f"student name is{self.name}")



gradu_student=Passout_Students("karimullah",12, "main")
print(gradu_student.__dict__)

student1.get_data()
gradu_student.get_data()