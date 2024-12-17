#Task 2
Student_names = ["Alice", "Ben", "Cara", "David", "Eva"]
Activities = ["hillwalking", "canoeing", "climbing", "hillwalking", "canoeing"]
Times_spent = [5, 3, 4, 6, 5]

def find_max(Times_spent):
    maximum_value = Times_spent[0]
    for counter in range(0, len(Times_spent)):
        if Times_spent[counter] > maximum_value:
            maximum_value = Times_spent[counter]
    print(f"The maximum time spent was {maximum_value} hours by {Student_names[counter - 1]} during {Activities[counter - 1]}")

def find_min(Times_spent):
    minimum_value = Times_spent[0] 
    for counter in range(len(Times_spent)):
        if Times_spent [counter] < minimum_value:
            minimum_value = Times_spent[counter]
    print(f"the minimum time spent was {minimum_value} hours by {Student_names[counter + 1]} during {Activities[counter + 1 ]}")

find_max(Times_spent)
find_min(Times_spent)

#task 3 
class Student:
    def __init__(self, name, activities, times_spent):
        self.name = name
        self.activities = activities
        self.times_spent = times_spent

students =[
Student("Alice", "Hillwalking", 5),
Student("Ben", "canoeing", 3),
Student("Cara", "climbing", 4),
Student("David", "hillwalking", 6),
Student("Eva", "canoeing", 5)
]


def find_max(students):
    maximum = students[0]
    for counter in range(len(students)):
        if students[counter].times_spent > maximum.times_spent:
            maximum = students[counter]
    print(f"The maximum time spent was {maximum.times_spent} hours by {maximum.name} during {maximum.activities}")

def find_min(students):
    minimum = students[0]
    for counter in range(len(students)):
        if students[counter].times_spent < minimum.times_spent:
            minimum = students[counter]
    print(f"The minimum time spent was {minimum.times_spent} hours by {minimum.name} during {minimum.activities}")

find_max(students)
find_min(students)

#play button not working???




