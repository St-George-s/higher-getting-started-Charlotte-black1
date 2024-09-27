# i have finished these 
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

