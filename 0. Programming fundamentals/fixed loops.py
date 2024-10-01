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
for i in range (10):
    age = int(input(f"Please enter the age of person {i+1}: "))
    print (age)

# question 8 
for i in range (10):
    age = int(input(f"Please enter the age of person {i+1}: "))
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