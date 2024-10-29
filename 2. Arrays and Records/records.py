#defining a record called bicycle (create a class)
class Bicycle:
    def __init__(self, brand, model, frame_size, type, price, electric_assist):
        self.brand = brand
        self.model = model
        self.frame_size = frame_size
        self.type = type
        self.price = price
        self.electric_assist = electric_assist

#created an instance of bicycle
my_variable = Bicycle("bmx", "10", 5, "extra light", 200, True)

print (my_variable.frame_size)

my_new_variable = Bicycle("road bike", "10", 10, "extra light", 500, True)
print (my_new_variable.electric_assist)