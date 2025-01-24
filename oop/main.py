# now lets creat our first class

class Item:
# the self here is a constant parameter when creating methods in our class. this passes the object/instance of the class as the first parameter
    def calc_total_price(self, price, quantity):
        return price * quantity


# now to create an instance of this class we say
item1 = Item()
# now we assign attributes to the object
item1.name = "Phone"
item1.price = 50000
item1.quantity = 7
#lets call the method here
print(item1.calc_total_price(item1.price, item1.quantity))
# now to create another instance

# now to create an instance of this class we say
item2 = Item()
# now we assign attributes to the object
item2.name = "Laptop"
item2.price = 80000
item2.quantity = 9