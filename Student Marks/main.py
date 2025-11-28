import csv

class Student:
    FILE_PATH = r'Python-Training/Student Marks/students.csv'
    def __init__(self):
        open(self.FILE_PATH, 'a').close()

    def view_data(self):
        with open(self.FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            print("student records")
            for row in reader:
                print(row)


    def add_data(self):
        num = int(input("enter number of students to add: "))
        data_list = []

        for i in range(num):
            print(f"enter data for student {i+1}")
            name    = input("name: ")
            rollno  = input("roll No: ")
            classs  = input("class: ")
            section = input("section: ")
            data_list.append([name, rollno, classs, section])

        with open(self.FILE_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)

        print("Data added successfully!")


    def update_data(self):
        roll = input("enter roll number to update: ")

        updated_rows = []
        found = False

        with open(self.FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == roll:
                    found = True
                    print("\nEnter new updated data:")
                    name    = input("name: ")
                    classs  = input("class: ")
                    section = input("section: ")
                    updated_rows.append([name, roll, classs, section])
                else:
                    updated_rows.append(row)

        if not found:
            print("record not available")
            return

        with open(self.FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        print("record updated")


    def delete_data(self):
        roll = input("enter roll number to delete: ")

        updated_rows = []
        found = False

        with open(self.FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] != roll:
                    updated_rows.append(row)
                else:
                    found = True

        if not found:
            print("record not found")
            return

        with open(self.FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

        print("Record deleted")



stud = Student()

while True:
    print("Student data menu")
    print("1   view data")
    print("2   add data")
    print("3   update data")
    print("4   delete data")
    print("5   exit")

    choice = input("Enter choice: ")

    if choice == "1":
        stud.view_data()
    elif choice == "2":
        stud.add_data()
    elif choice == "3":
        stud.update_data()
    elif choice == "4":
        stud.delete_data()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("plx enter 1 - 5 ")
