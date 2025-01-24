#program to add 2 numbers
first_num = input("Enter first number? ")
second_num = input("Enter second number? ")

result = float(first_num) + float(second_num)
print(result)
# to concatenate result to string, convert result into string
print("Sum is "+ str(result))

# you can also change type of input from string. i.e
first_num = float(input("Enter first number: "))
# now the string is converted to float 