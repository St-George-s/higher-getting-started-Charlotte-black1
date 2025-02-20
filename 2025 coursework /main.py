import csv

class orders:
    def __init__(self, orderNum, date, email, option, cost, rating):
        self.orderNum = orderNum
        self.date = date
        self.email = email
        self.option = option
        self.cost = cost 
        self.rating = rating

def read_from_file ():
    orders = []
    with open ("coursework /orders.txt", "r") as file:
        rows = csv.reader (file)
        for row in rows:
            newRecord = orders(row[0], row[1], row[2], row[3], row[4], row[5])
            orders.append(newRecord)
        return orders




