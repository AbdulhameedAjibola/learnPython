course = "Python is good";

#test out some string methods
#convert string to uppercase
print(course.upper())

# find a character or a sequence of character in the string. this returns the index of the first occurence of the character
print(course.find('y'))
#sequence
print(course.find("go"))

#replace something in a string, if what we're tring to replace doesnt exist, nothing happens
print(course.replace("is", "iz"))

#using the in operator, can also be used to check for something in a string, returns a boolean value instead of the index
print("python" in course)

# since a string is a character array, to get a particular letter in the string, we use the string name and a square brackets to specify index
print(course[4])