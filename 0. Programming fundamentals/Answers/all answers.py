#  task one 
#  question 1 
for i in range(10):
    print ("Charlotte")

# question 2 
name = input("What is your name: ")
for i in range (1000):
    print (name) 

# question 3 
name = input("What is your name: ")
print ("Hello")
for i in range (1000):
    print (name)

# question 4 
for i in range (1,13):
    print ((8*i))

# question 5 
for i in range (1,1001):
    print (str(8*i))

# question 6 
for i in range (1,13):
    print (str(8) + "x" + str(i) + "=" + str(8*i))

# question 7 
ages = []
for i in range (10):
   age = int(input(f"Please enter the age of person {i+1}: "))
   ages.append (age)
for age in ages:
    print (age)

# question 8 
ages = []
for i in range (10):
   age = int(input(f"Please enter the age of person {i+1}: "))
   ages.append (age)
for age in ages:
    print (age+10)

# question 9 
total_age = 0
for i in range(10):
    age = int(input(f"Please enter the age of person {i+1}: "))
    total_age += age
print("The total age is: " + str(total_age))

# question 10 - probably a shorter way to do this
for i in range (1,13):
    for j in range (1,13):
        print (str(j) + "x" + str(i) + "=" + str(j*i))

# task two 
# question 1 
code = input("Please enter your three letter code: ")
while code != "rzy":  
    print ("Code not accepted")
    code = input("Please enter your three letter code: ")
print ("Code accepted")

# question 2 
code = int(input("please enter your four digit code: "))
while code != 4003:
    print ("Code not accepted")
    code = int(input("Please enter your four digit code: "))
print ("Code accepted")

# question 3 
age = int(input("Please enter your age: "))
while age <15:
    print ("Age not accepted")
    age = int(input("Please enter your age: "))
print ("Age accepted")

# question 4 
password = input("Please enter your password: ")
while len(password) < 5:
    print ("Password is too short ")
    password = input("Please enter your password: ")
print ("Password accepted")

# question 5 
watch = input("Would you like to keep watching Modern Family: ")
while watch == ("yes"):
    print ("playing another episode")
    print ("some time later...")
    watch = input("Would you like to keep watching Modern Family: ")
print ("See you later")

# question 6 
ammount_offered = int(input("Please give me some money: £"))
while ammount_offered < 101:
    print ("That's not enough, more please")
    ammount_offered = ammount_offered + int(input("Please give me some money: £"))
print ("ammount accepted, Thank you!")

# task three
# question 1 and 2 
age = int(input("Please enter your age: "))
if age >= 18:
    print ("You are eligable for movies with a rating of 18 or below")
elif age >=15:
    print ("you are eligable for movies with a rating of 15 or below")
else: print ("you are not eligable for movies with an 18 or 15 rating")

# question 3 
feeling = input("How are you feeling tody: ")
if feeling == ("happy"):
    print ("That's good!")
elif feeling == ("sad"):
    print ("Oh, I'm sorry, eat some chocolate")
elif feeling == ("tired"):
    print ("Have an early night tonight")
elif feeling == ("bored"):
    print ("how about watching some TV?")
elif feeling == ("excited"):
    print ("what are you excited for?")
elif feeling == ("hungry"):
    ("would you like something to eat?")
else:
    print ("okay, have a nice day")

#question 5 
number_one = int(input("Please enter a number: "))
number_two = int(input("please enter another number: "))
procedure = input("would you like to add, subract, multiply or divide the numbers: ")
if procedure == ("+"):
    print (number_one, "+", number_two, "=", number_one+number_two)
elif procedure == ("-"):
    print (number_one, "-", number_two, "=", number_one-number_two)
elif procedure == ("x"):
    print (number_one, "x", number_two, "=", number_one*number_two)
elif procedure ==("/"):
    print (number_one, "/", number_two, "=", number_one/number_two)

#task 4 
#question 1, 1.1
temperature = int(input("What is the temperature today: "))
sunny = input("Is it sunny today: ")
print ((sunny == ("yes")) and (temperature >15))

#question 1, 1.2
temperature = int(input("What is the temperature today: "))
raining = input("Is it raining today: ")
print ((raining == ("yes")) or (temperature >15))

#question 1, 1.3
apples = int(input("how many apples are there: "))
print (apples >10)

#question 2, 2.1
age = int(input("How old are you: "))
licence = input("Do you have a driving licence: ")
print ((age >18) and (licence == ("yes")))

#question 2, 2.2
speed = int (input("what is the speed of the car: "))
raining = input("Is it raining: ")
print ((speed >60) or (raining == ("no")))

#question 2, 2.3
hours = int(input("how many hours did you study: "))
prepared = input("Do you feel prepared: ")
print ((hours >5) or (prepared ==("yes")))

#question 3, 3.3
sunny = input("Is it sunny today: ")
weekend = input("Is it the weekend: ")
print ((sunny == ("yes") and weekend == ("yes")) or (sunny == ("no") and weekend == ("no")))

#advanced instructions 
#number guessing game
import random
target_number = random.randint(0,100)
guess = int(input("Pick a number between 0 and 100: "))
while guess > target_number:
    print ("too high")
    guess = int(input("Pick a lower number: "))
while guess < target_number:
    print ("too low")
    guess = int(input("Pick a higher number: "))
while guess == target_number:
    print ("well done! you got the right number")

#task one 
#question 1
numbers = [1, 2, 3, 4, 5]
print (numbers)

#question 2 
numbers = [10, 20, 30, 40, 50]
print (numbers[0], numbers[4])

#question 3 
numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers[2])

#question 4 
numbers = [5, 10, 15, 20, 25]
for number in numbers:
    print (numbers)

#question 5 
total = 0
numbers = [2, 4, 6, 8, 10]
for number in numbers:
    total = (total)+(number)
print (total) 

#question 6 
numbers = [12, 45, 2, 9, 50, 33]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print (max) 

#question 7 
numbers = [18, 4, 22, 9, 31, 15]
min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print (min) 

#question 8 
numbers = [3, 6, 9, 12, 15]
numbers.reverse()
print (numbers)

#question 9 
numbers = [7, 14, 21, 28, 35]
for number in numbers:
    print (number == 21)

#question 10
first_array = [1, 2, 3]
second_array = [4, 5, 6]
print (first_array + second_array)

#question 11 
numbers = [5, 3, 8, 1, 2]
numbers.sort()
print (numbers)

#question 12
numbers = [3, 3, 3, 3, 3]
print (numbers == numbers)

#question 13 
numbers = [10, 20, 30, 40, 50]
for index in range(len(numbers)):
    number = numbers[index]*2 
    print (number)

#question 14 
numbers = [8, 6, 7, 5, 3, 0, 9]
numbers.remove (int(3))
print (numbers)

#question 15
#option 1
numbers = [12, 24, 35, 24, 88, 120, 155]
new_numbers = []
for index in range(len(numbers)):
    if numbers[index] != 24:
     new_numbers.append(numbers[index])
numbers = new_numbers
print (numbers)

#option 2
numbers = [12, 24, 35, 24, 88, 120, 155]
length = len(numbers)
index = 0
while index < length:
   if numbers[index] == 24:
    numbers.remove(24)
    length = length -1
   index = index+1
print(numbers)

#question 16 
numbers = [5, 12, 7, 5, 5, 7]
print (numbers.count (5))

#question 17 
numbers = [9, 3, 6, 1, 7]
for index in range(len(numbers)):
    if numbers[index] == 6:
        print(index)

#question 18 
numbers = [2, 4, 6, 8, 10]
total = 0
for index in range(len(numbers)):
    total = total + numbers[index]
print (total)

#question 19 
numbers = [15, 22, 13, 14, 22, 45]
for index in range(len(numbers)):
    if numbers[index] == 22:
        print (index)  

#question 20
names = ["Alice", "Bob", "charlie"]
scores = [85, 92, 78]
for index in range(len(names)):
    print (names[index], scores[index])

#travel information task 
def get_destination():
    return input ("where would you like to go: ")
def get_people():
    return input ("how many people will come with you: ")
def get_travel():
    return input ("how would you like to travel: ")
def show_information(destination, people, travel):
    print (f"you are going to {destination} with {people} other people and will travel by {travel}")

keep_asking = ("yes")
while keep_asking != ("END"):
    destination = get_destination()
    people = get_people()
    travel = get_travel()

    show_information(destination, people, travel)
    keep_asking = input ("would you like book another holiday(type END if no): ")

# question 1 
name = input ("what is your name: ")

#question 2
age = int(input("how old are you: "))
while age <10 or age >30 :
    print ("age invalid, try again: ")
    age = int(input("how old are you: "))

#question 3 
with open("0. Programming fundamentals/Answers/people.txt", "a") as file:
    file.write(str(name))
    file.write(str(age))
    file.close()

#parallel arrays
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Harry", "Ivy", "Jack", "Katie", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tara", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zach", "Sophie", "Thomas", "Natalie", "Ellie", "Lucas", "Isabella", "Henry", "Amelia", "Leo", "Ella", "Oscar", "Charlotte"]
ages = [25, 30, 22, 35, 28, 40, 33, 29, 26, 31, 27, 34, 23, 36, 32, 39, 21, 38, 37, 24, 42, 45, 41, 43, 44, 46, 33, 29, 35, 26, 31, 30, 28, 36, 27, 32, 34, 23]
colours = ["blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red", "green", "yellow", "orange", "purple", "blue", "red"]

between_30_and_40_names = []
between_30_and_40_ages = []
between_30_and_40_colours = []

for index in range(len(ages)):
    if ages[index]>30 and ages[index]<40:
     between_30_and_40_names.append(names[index])
     between_30_and_40_ages.append(ages[index])
     between_30_and_40_colours.append(colours[index])

print(between_30_and_40_names)
print(between_30_and_40_ages)
print(between_30_and_40_colours)
    
with open("0. Programming fundamentals/Answers/people_in_age_range.txt", "w") as file:
   for index in range(len(names)):
      file.write(str(names[index]))
      file.write(",")
      file.write(str(ages[index]))
      file.write(",")
      file.write(str(colours[index]))
      file.write(str(" "))
      file.close 

#player record programe
class Player:
  def __init__(self, uniqueID, score, minutes, speed, strength, agility):
    self.uniqueID: str = uniqueID
    self.score: int = score
    self.minutes: float = minutes
    self.speed: int = speed
    self.strength: int = strength
    self.agility: int = agility

player_one = Player ("charlotte10", 100, 4.21, 62, 45, 97)

print (player_one.uniqueID, player_one.score, player_one.minutes, player_one.speed, player_one.strength, player_one.agility)

#array manipulation program 
numbers = [10, 20, 30, 40, 50]
numbers[2] = 35
print (numbers)
