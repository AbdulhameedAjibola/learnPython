# here we will see how we validate the arguments received from the constructor using assert statements

class Device:
    def __init__(self, name: str, price: float, quantity: float):
        #Run validations on received arguments
        # so here we are using our assert statement to say that we do not want to receive any negative inputs for price and quantity
        # i.e, inputs less than 0
        # so to specify an error message for our assert keyword, we can pass it as a second argument
        assert price >= 0,f"price {price} is nor a real number! "
        assert quantity >= 0, f"quantity {quantity} is nor a real number! "

        # Assign variables to self object
        self.name = name
        self.price = price
        self.quantity = quantity

# if i run this code below the program returns an assertion error. However we can specify our own assert error messages also, see example above
device1 = Device("John", -1, -4)
