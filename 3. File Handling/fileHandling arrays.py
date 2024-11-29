import csv

# Store in Parallel Arrays
#students
student_id = []
firstname = []
lastname = []
grade =[]

def read_from_file():
    with open("3. File Handling/students.csv", "r") as f:
        rows = csv.reader(f)
        print(rows)
        next(rows)
        for row in rows:
            student_id.append(row[0])
            firstname.append(row[1])
            lastname.append(row[2])
            grade.append(row[3])
        print (student_id)

read_from_file()

#athletes 
entry_id = []
location = []
forename = []
surname =[]
jumps = []

with open("3. File Handling/athletes.csv", "r") as f:
    rows = csv.reader(f)
    print(rows)
    next (rows)
    for row in rows:
        entry_id.append(row[0])
        location.append(row[1])
        forename.append(row[2])
        surname.append(row[3])
        jumps.append(int(row[4]))
    print (entry_id)
    print (jumps)