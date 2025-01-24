# class atributes are used to create attributes that will be shared across all the instances of a class
# a class attribute is an attribute that belons to the class itself but can alsobe accessed from the instance level as well
# variables that are initialized through the constructor are known as instance attributes
class Discount:
    # what we see below is a class attribute, this is an attribute/ variable that belongs to the class itself
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
       self.price= self.price * self.pay_rate
        # in this method, it is noticed that we cannot access the class attribute directly through the method
        # the class attribute can only be accessed through the class levels or instance levels

# if we want to print out what is in thw class, we will reference the varialble theough the class itself
print(Discount.pay_rate)
'''
 we can also access this class attribute through the instance level
discount = Discount()
print(discount.pay_rate)
# we can use the __dict__ magic attribute to print out all the attributes belonging to a particular object, or class
print(Discount.__dict__) # all attributes for class level
print(discount.__dict__) # all attributes for instance level
'''

discount1 = Discount("Itel", 200)
discount1.apply_discount()
print(discount1.price)

# now lets say we want to change the class atribute for only one instance, we can do so as ssated below
discount2 = Discount("Koenisegg", 4000, 15)
discount2.pay_rate = 0.7 # here we have changed the class attribute from 0.8 to 0.7 for this instance only
discount2.apply_discount()
print(discount2.price)