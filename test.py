import csv

#Make an array of records 
class Sighting:
    def __init__(self, town, mammal, date, age):
        self.town = town 
        self.mammal = mammal
        self.date = date
        self.age = age 

#Append information from the file into records 
def read_from_file ():
    sightings = []
    with open ("./mammals.txt", "r") as f:
       rows = csv.reader (f)
       for row in rows:
           newRecord = Sighting (row[0], row[1], row[2], row[3])
           sightings.append (newRecord)
    return sightings

sightings = read_from_file()

# record = sightings[23]
# dateFromRecord = record.date
# monthFromDate = dateFromRecord[3:5]
# print(monthFromDate)

# myString = "charlotte"
# print(myString[0:5])


for sights in sightings:
    myDate = sights.date[6:8]
    print(sights.date)
    print(myDate)

