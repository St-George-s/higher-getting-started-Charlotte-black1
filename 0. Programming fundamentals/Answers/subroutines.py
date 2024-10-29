#examples
# Procedure as nothing returned
def mySubProgram(myParameter):
    print("hello " + myParameter)

# Function
def myNewSubProgram(myParameterOne, myParamterTwo):
    return myParameterOne * myParamterTwo

mySubProgram("Charlotte")
mySubProgram("Bob")
mySubProgram("Mr W")
mySubProgram("Sasha")
mySubProgram("Graham")

answer = myNewSubProgram(10,5)
print(answer)

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