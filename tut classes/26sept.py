'''


number = 10
while number >= 0:
    print(number)
    number = number - 1

# timetable
digit = int(input("Enter a number"))

starting_number = 1
ending_number = 12

while starting_number <= ending_number:
    value = digit * starting_number
    print(f"{digit} * {starting_number} = {value}")
    starting_number+=1
'''
#factorial
value = 1
x = 1
integer = int(input("enter number to find factorial"))

while integer > value:
    x *= integer

    integer-=1
print(x)

