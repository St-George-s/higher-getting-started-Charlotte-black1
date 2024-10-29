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
# Option 1
numbers = [12, 24, 35, 24, 88, 120, 155]
new_numbers = []
for index in range(len(numbers)):
    if numbers[index] != 24:
     new_numbers.append(numbers[index])
numbers = new_numbers
print (numbers)

# Option 2
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

#array manipulation program 
numbers = [10, 20, 30, 40, 50]
numbers[2] = 35
print (numbers)