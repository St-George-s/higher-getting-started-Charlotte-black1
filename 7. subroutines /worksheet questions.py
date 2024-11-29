#question 3a)
#function with formal parameters 
def greet (name, age):
    print (f"hello, {name}! you are {age} years old.")
#calling the function with actual parameters 
greet ("Alice", 25)

#question 3b)
def modify_value(num):
    num = num * 2
    return num 

value = 10 
result = modify_value(value)
print(value, result)

#question 3c)
def add_friend(friends_list, friend_name):
    friends_list.append(friend_name)
    add_friend(my_friends, "Charlie")
    print(my_friends)

#question 4 