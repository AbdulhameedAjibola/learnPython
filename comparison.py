#most operators here, return a boolean
#lets check it out

#the greater than operator
x = 3 > 2
print(x)

# the less than operator
x = 4 < 7
print(x)

# greater than or equal to
x = 15 >= 5
print(x)

# the less than or equals to operator
x = 3 <= 5
print(x)

# the equality operator, single is assignment operator, double is equality operator
x = 4 == 5
print(x)

# the not equals to operator
x = 3 != 5
print(x)


# LOGICAL OPERATORS

# the AND operator: its used to evaluate between two conditions. If both conditions evaluate true, the result will be true
price = 250
print(price < 200 and price > 220)

# the OR operator: its used to evaluate if one or the other condtion is true. i.e its checks two conditions and returns true if one of them is true
price = 250
print(price < 100 and price > 220)

# we have the NOT operator also, inverts the result of the operation
price = 5
print(not price < 3)