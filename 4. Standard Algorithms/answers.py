#Task 1 
times_spent = [5, 3, 4, 6, 5]

def find_max(times_spent):
    maximum_value = times_spent[0]
    for counter in range(1, len(times_spent)):
        if times_spent[counter] > maximum_value:
            maximum_value = times_spent[counter]
    print(f"The maximum time spent was {maximum_value}")

def find_min(times_spent):
    minimum_value = times_spent[0]
    for count in range (len(times_spent)):
        if times_spent[count] < minimum_value:
            minimum_value = times_spent[count]
    print(f"The minimum time spent was {minimum_value}")

def linear_search(times_spent, item_to_find):
    found = False 
    counter = 0 
    array_size = len(times_spent)
    while counter < array_size and not found:
        if times_spent[counter] == item_to_find:
          found = True
        else:
            counter += 1
    if found:
        print(f"The time {item_to_find} hours was found in position {counter}")
    else:
        print("item not found")

def count_occurrences(times_spent, item_to_find):
    number_found = 0 
    for item in times_spent:
        if item == item_to_find:
            number_found += 1 
    print (f"The time {item_to_find} hours appeared {number_found} times in the array")

find_max(times_spent)
find_min(times_spent)
linear_search(times_spent, 4)
count_occurrences(times_spent, 5)
find_max([1, 2, 3, 4])