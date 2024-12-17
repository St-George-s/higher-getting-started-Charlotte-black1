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
def multiply_list(list, multiplyer_number):
    for count in range(len(list)):
     list[count] = 10
     return list 

list = [0,1,2]
print (multiply_list(list, 10))

#friend finder app 
#question 2a)
registered_users = []
def register(username, password):
    user_data = {
        'username': username,
        'password': password
    }
    registered_users.append(user_data)

register("Alice", "password123")
print(registered_users)

#question 2b)
logged_in_user = None 

def login(username, password):
   global logged_in_user
   for user in registered_users:
    if user ['username'] == username and user ['password'] == password:
        logged_in_user = username
        return True 
   return False 

if login ("Alice", "password123"):
    print (f"{logged_in_user}is now logged in!")

#question 2c)
friend_requests = {}

def send_friend_request(sender, reciever): 
   if reciever in friend_requests:
      friend_requests[reciever].append(sender)
   else:
      friend_requests[reciever] = [sender]

send_friend_request("Alice", "Bob")
print (friend_requests)

#question 2d)
friends_list = {}

def accept_friend_request(reciever, sender):
    if sender in friend_requests[reciever]:
    #adds to friends list 
        if reciever in friends_list:
          friends_list [reciever].append(sender)
        else:
          friends_list[reciever] = [sender]
        if sender in friends_list:
          friends_list[sender].append(reciever)
        else: 
           friends_list[sender] = [reciever]
    #remove from friends requests 
        friend_requests[reciever].remove(sender)
accept_friend_request ("Bob", "Alice")
print(friends_list)