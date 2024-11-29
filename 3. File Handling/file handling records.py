import csv

# Store in array of records
class Student:
    def __init__(self, student_id, firstname, lastname, grade):
        self.student_id = student_id
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade

students =[]

with open("3. File Handling/students.csv", "r") as f:
    rows = csv.reader(f)
    print(rows)
    next(rows)
    for row in rows:
       newRecord = Student(row[0], row[1], row[2], row[3])
       students.append(newRecord)

    print (students[3].student_id)