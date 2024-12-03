PI = 3.14

# Procedure with 1 parameter
def calculateAreaCircle(radius):
    print(PI * radius ** 2)

# Call of the procedure
calculateAreaCircle(10)

# Function with 2 paramters
def calculateAreaRectangle(length, breadth):
    return length * breadth

# Call of the function and print returned value
print(calculateAreaRectangle(10,10))

# Call of the function and store returned value
result = calculateAreaRectangle(10,10)
print("My result was " + str(result))

for i in range(10):
    print(i)

