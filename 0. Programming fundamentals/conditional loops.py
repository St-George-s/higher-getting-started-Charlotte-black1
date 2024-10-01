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