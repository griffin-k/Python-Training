import csv

student_data = r'File Handling/students.csv'


with open(student_data, 'w' , newline='') as file:
    csv_writer = csv.writer(file, delimiter=',')

    no_of_students = int(input("plz enter the no of students: "))
    list_of_students = []


    
    for i in range(no_of_students):
        print(f"enter the data for {i} student")
        name    = input("Enter name: ")
        rollno  = input("Enter roll no: ")
        classs  = input("Enter class: ")
        section = input("Enter section: ")

        

        list_of_students.append([name, rollno, classs, section])

 
    csv_writer.writerows(list_of_students)
