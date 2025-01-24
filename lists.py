# lists, also knows as array is used to store multiple data in one variable name

names = ["Amaka", "Collins", "Emeka", "Adufe"]
print(names)
# to print individual elements, you add a bracket and then specify the index in the list
print(names[2])

# in python, we can also use negative indexes, for example, if we use -1, it returns the last index of the array
# in essence, it reverses the array, -1 for the last element, -2 for the next after the last etc
print(names[-1])

# we can also edit the content of a list. e.g
names[2] = "Becky"

# we can also specify items to be printed out from an array by specifying the stat index and the end index
# we can also specify a starting index and then it prints from that index to the end of the array
print(names[0:2])

#LIST METHODS
numbers = [1,2,3,4,5,6,7]
# to add to list. the append method always adds to the end of the list
numbers.append(6)

# we can also insert into the list by specifying position, and the object to be inserted
numbers.insert(2, 44)
print(numbers)

# we can also remove items from the list
numbers.remove(3)
# we can also delete the last item on this list by using the pop method
numbers.pop()

# to remove all items in list, we use
numbers.clear()

# we use in operator to check if a particular value is in the list. This returns a boolean value
print(44 in numbers)

# to get the length of the list we use
print(len(numbers))
# the extend functions allows you to append a list the to the end of another list
names.extend(numbers)
# how to get the index of an item in a list
print(names.index("Amaka"))
# the sort function helps to sort the list in ascending order
names.sort()

# we can use the copy method to duplicate an array
names2 = names.copy()