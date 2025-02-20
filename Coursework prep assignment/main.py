import csv 

class Member: 
    def __init__(self, forename, surname, distance):
        self.forename = forename 
        self.surname = surname
        self.distance = distance

def read_from_file (): 
    members = []
    with open ("Coursework prep assignment/members.txt","r") as file:
        rows = csv.reader (file)
        for row in rows:
            newRecord = Member (row[0], row[1], row[2])
            members.append (newRecord)
    return members

def max_distance (members):
    furthest = members[1].distance 
    for i in range (1,len(members)):
        if members[i].distance > furthest:
            furthest = members[i].distance
    
def results (members, furthest):  
    with open ("Coursework prep assignment/members.txt", "a") as file:
        file.write ("The prize winning members are: ")
        for i in range (0,len(members)):
            if members[i].distance > 0.7*furthest:
                file.write (f"{members[i].forename} {members[i].surname}")


members = read_from_file ()
max_distance (members)

