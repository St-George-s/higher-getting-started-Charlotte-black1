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