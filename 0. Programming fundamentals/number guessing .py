#advanced instructions 
#number guessing game
import random
target_number = random.randint(0,100)
print(target_number)

guess = int(input("Pick a number between 0 and 100: "))

while target_number != guess:
    if guess > target_number:
        print ("too high")
        guess = int(input("Pick a lower number: "))
    elif guess < target_number:
        print ("too low")
        guess = int(input("Pick a higher number: "))

print ("well done! you got the right number")
