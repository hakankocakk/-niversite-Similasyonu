import sqlite3

class University():
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.status = True


    def run(self):
        self.menu()

        choice = int(input("Select: "))

        choices = {1: self.addStudent,
                   2: self.deleteStudent,
                   3: self.updateStudent,
                   4: self.showStudent,
                   5: self.exit}

        if choice in choices:
            choices[choice]()


    def menu(self):
        print(f"***** {self.name} Administration System *****")
        print("\n1) Add Student\n2)Delete Student\n3)Update Student\n4)Show\n5)Exist")

        
    def choice(self):
        while True:
            try:
                process = int(input("Select: "))
                if process < 1 and process > 5:
                    print("Operation number must be between 1 -5, please select correct number!")
                    continue
                break

            except ValueError:
                print("Operation is must be integer number. Please ")

        return process
    

    def addStudent(self):
        studentId = int(input("Student Id: "))
        studentName = input("Student Name: ")
        studentSurname = input("Student Surname: ")
        studentFaculty = input("Student Faculty: ")
        studentDepartment = input("Student Department: ")
        studentNumber = int(input("Student Number: "))
        studentEducationtype = input("Student Education of Type: ")
        studentStatus = input("Student Status: ")
        with sqlite3.connect("University.db") as conncect:
            cursor = conncect.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS students(studentId INT, studentName TEXT, studentSurname TEXT, studentFaculty TEXT, studentDepartment TEXT, studentNumber INT, studentEducationtype TEXT, studentStatus TEXT)")
            cursor.execute("INSERT INTO students (studentId, studentName, studentSurname, studentFaculty, studentDepartment, studentNumber, studentEducationtype, studentStatus) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (studentId, studentName, studentSurname, studentFaculty, studentDepartment, studentNumber, studentEducationtype, studentStatus))
            conncect.commit()

        
    def deleteStudent(self):
         with sqlite3.connect("University.db") as conncect:
            cursor = conncect.cursor()
            cursor.execute("SELECT * from students")
            for student in cursor.fetchall():
                print(student)
            while True:
                try:
                    deleteStudent = int(input("Please enter the student id to be deleted: "))
                    if len(str(deleteStudent)) != 11:
                        print("Student ID must be 11 digits. Please enter correctly.")
                        continue
                    break
                except ValueError:
                    print("Student Id is must be integer number.")
            cursor.execute(f"DELETE from students WHERE studentId == {deleteStudent}")
            cursor.execute("SELECT * from students")
            for student in cursor.fetchall():
                print(student)
            conncect.commit()


    def updateStudent(self):
        with sqlite3.connect("University.db") as conncect:
            cursor = conncect.cursor()
            cursor.execute("SELECT * from students")
            for student in cursor.fetchall():
                print(student)
            while True:
                try:
                    updatestudent = int(input("Please enter the student id to be updated: "))
                    if len(str(updatestudent)) != 11:
                        print("Student ID must be 11 digits. Please enter correctly.")
                        continue
                    break
                except ValueError:
                    print("Student Id is must be integer number.")

                           
            while True:
                try:
                    update = int(input("\n1)studentName\n2)studentSurname\n3)studentFaculty\n4)studentDepartment\n5)studentNumber\n6)studentEducationtype\n7)studentStatus\nSelect: "))
                    if update < 1 and update > 7:
                        print("Operation number must be between 1 -5, please select correct number!")
                        continue
                    break
                except ValueError:
                    print("Operation is must be integer number. Please ")

            while True:
                try:
                    if update == 5:
                        updatevalue = int(input("Value: "))
                    else:
                        updatevalue = input("Value: ")
                    break
                except ValueError:
                    print("Please enter correct")

            Updates = {1: "studentName",
                   2: "studentSurname",
                   3: "studentFaculty",
                   4: "studentDepartment",
                   5: "studentNumber",
                   6: "studentEducationtype",
                   7: "studentStatus"}
  
            cursor.execute(f"UPDATE students SET {Updates[update]} = {updatevalue} WHERE  studentId = {updatestudent}")
            cursor.execute("SELECT * from students")
            for student in cursor.fetchall():
                print(student)


    def showStudent(self, by):
        with sqlite3.connect("University.db") as conncect:
            cursor = conncect.cursor()
            cursor.execute("SELECT * from students")
            for student in cursor.fetchall():
                print(student)
    def exit(self):
        self.status = False



Uni = University("Yildiz Technical University", "Turkey")

while Uni.status:
    Uni.run()
