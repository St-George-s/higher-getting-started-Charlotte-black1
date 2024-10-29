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
      