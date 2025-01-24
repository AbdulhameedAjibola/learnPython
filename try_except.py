'''
in python, the try except is used for catching errors without terminating the flow of the program
for the two lines of code written below, if user enters anything other than an integer, it terminates the code
and then prints out an error message
but with a try except, it catches/accounts for the error without disturbing the flow of the program
'''

# number = int(input("enter a number: "))

# print(number)

# see example below
try:
    number = int(input("enter a number: "))

    print(number)
    print("Dele is a good boy")
except:
    print("Invalid input")

'''
in the code snippet above the except keyword is being highlighted, which means its a broad exception cacher
so, in python, there are various exceptions for various conditions which are specific to each other, see example below
so specific excepts, catch specific errors in the code  
'''
try:
    value = 10/0
    digit = int(input("Enter your number: "))
    print(digit)
except ZeroDivisionError:
    print("Indivisible by zero")
except ValueError:
    print("Invalid Input")

# so we can also store the error message in a variable and jusr print out the error message, we do this using the as keyword
try:
    answer = 10/0
    
except ZeroDivisionError as err:
    print(err)