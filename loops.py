# # the while loop
# # the while loop is used to iterate over a particular block of code for when the condition remains true
#
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
#
# # here we're going to multiply an asterik by the value of i, this prints out the * correspondent to the value of i

i = 10
while i < 10:
     print(i)
     i = i + 1


# FOR LOOPS
foods = ["Banga", "ofe Nsala", "Pepper soup", 1, 3, 5]
# to use the for loop, we crate a variable to hold each index in the list, the block of code executes as long as condition is true

for item in foods:
    print(item)
# in python we can also check if something is inside of something i.e

def translator(sentence):

    translation = ""
    for letter in sentence:
        if letter in "AEIOUaeiou":
            translation = translation + "ba"
        else:
            translation = translation + letter

    return translation

print(translator(input("Enter a Phrase ")))
