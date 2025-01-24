# a constructor is used to initialize variables in a class once an instance is created
# on creation of any instance/ object of the class, whatever is in the init method gets executed
# it is usually preceded by double under scores, and it ends with double underscores too
# there are a collection of similar methods which have similar syntax, and they are called magic methods

class Device:
    # here, we've initialized the variables to be used in the constructor, and then once we create an object, we simply
    # pass the variables as parameters to the object
    #it is best practice to declare variable to be used in the class in the constructor, and then initialize then on object creation
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    # after we have instantiated our variable through a constructor,we dont need to take them in as parameters anymore
    # we can just reference it from the constructor
    def amount(self):
        return self.quantity * self.price



device1 = Device("korede", 1000, 34)
print(device1.amount())
# although we declared our variables through a constructor, we are still allowed to add more variables to specific instances
device2 = Device("Laptop", 250, 22)
device2.has_keyboard = False
