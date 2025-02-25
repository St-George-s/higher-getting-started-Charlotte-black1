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
    
#following the refinements section for question 1.c) 
def find_first_rating (orders):
    position = -1
    index = 0
    month_to_search = input("Please enter the first three letters of the month: ")
    while position == -1 and index < len(orders):
        if orders[index].date == month_to_search and orders[index].rating == 5:
            position = index
        index = index =+ 1  
    print (position)
    return (position)
   
#def write_to_file (orders, position):
#   with open ("2025 coursework /winning customer.txt", "r") as file:
#        if position.orderNum> 0:
#          file.write (orders.orderNum, orders.email, orders.cost)
#        else:
#         file.write ("No winner")
#   file.close 

#def countOption (orders, option_to_find):
#    number_found = 0 
#    for option in orders:
#        if option == option_to_find:
#            number_found += 1
#    print (f"there were {number_found} orders that selected the {option_to_find} option")
    

orders = read_from_file ()
find_first_rating (orders)
#write_to_file (orders, find_first_rating(orders))
#countOption (orders, "Collection")



