import csv

class Order:
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost 
        self.rating = rating

#reads from file into array of records 
def read_from_file ():
    orders = []
    with open ("2025 coursework /orders.txt", "r") as file:
        rows = csv.reader (file)
        for row in rows:
            newRecord = Order(row[0], row[1], row[2], row[3], row[4], row[5])
            orders.append (newRecord)
    return orders

orders = read_from_file () 

#following the refinements section for question 1.c) 
#this finds the person who gave the first 5 star rating of the month 
def find_first_rating (orders):
    position = -1
    index = 0
    month_to_search = input("Please enter the first three letters of the month: ")
    while position == -1 and index < len(orders):
            monthFromDate = orders[index].date[3:6]
            ratingFromOrder = orders[index].rating
            if monthFromDate == month_to_search and ratingFromOrder == '5':
                position = index
            index = index + 1 
    return (position)


# this writes the winner's details in a file 
def write_to_file (orders, find_first_rating):
    position = find_first_rating(orders)
    with open ("2025 coursework /winning customer.txt", "w") as file:
        if position >= 0:
            file.write (f"{orders[position].orderNum}, ")
            file.write (f"{orders[position].email}, ")
            file.write (orders[position].cost)
        else:
            file.write ("No winner")
    file.close 

write_to_file (orders, find_first_rating)

#this counts how many people chose "delivery" or "collection" options
def countOption (orders, option_to_find):
    number_found = 0 
    for i in range (len(orders)):
        if orders[i].option == option_to_find:
            number_found += 1
    print (f"there were {number_found} orders that selected the {option_to_find} option")
    
countOption (orders, "Delivery")    
countOption (orders, "Collection")



