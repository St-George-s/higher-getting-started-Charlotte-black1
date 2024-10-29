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