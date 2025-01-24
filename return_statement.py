# the return statement allows us to return something back to whatever is calling the function
# the return keyword breaks us out of a function, so code written after it in a method will not be executed
def exponent(number):
   return pow(number, 2)


print(exponent(8))