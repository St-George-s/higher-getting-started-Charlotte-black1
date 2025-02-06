#1. b) 
#This isnt asked for in the question but it makes it easier to check
town = input ("please enter a town: ")
mammal = input ("please enter a mammal: ")

#This is how to capitalise a word (this is what the question was asking)
def capitalise (word):
    first_character = ord (word[0])
    if first_character > 97 and first_character < 122:
        first_character = first_character -32
        word = chr (first_character) + word [1:]
    print (word)
    return word 

#This is how to call the function (using when the user input at the start)
capitalise (town)
capitalise (mammal)


#1. c) 
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
    with open ("Coursework prep assignment/mammals.txt", "r") as f:
       rows = csv.reader (f)
       for row in rows:
           newRecord = Sighting (row[0], row[1], row[2], row[3])
           sightings.append (newRecord)
    return sightings

# This finds the oldest walker in the file         
def oldest_walker (sightings):
    maximum_value = sightings[0].age
    for i in range (1, len(sightings)):
        if sightings[i].age > maximum_value:
            maximum_value = sightings[i].age
    print (f"the oldest walker was {maximum_value} years old")

#This prints all the dates of all the sightings
def get_dates (sightings):
    for i in range(len(sightings)):
        print (sightings[i].date)

#This counts how many sightings there were on each date
def count_sightings (sightings):
    day_to_count = sightings[0].date
    count = 1
    for i in range (1, len(sightings)):
        if sightings[i].date == day_to_count:
            count += 1
        else:   
            print (f"there were {count} sightings on {day_to_count}")
            day_to_count = sightings[i].date
            count = 1
    print (f"there were {count} sightings on {day_to_count}")
       
#This calls all the procedures form question 1.b)
sightings = read_from_file ()
oldest_walker (sightings)
get_dates (sightings)
count_sightings (sightings)