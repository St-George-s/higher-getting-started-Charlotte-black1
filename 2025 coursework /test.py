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

record = orders[14]
dateFromRecord = record.date
monthFromDate = dateFromRecord[3:6]
print(monthFromDate)