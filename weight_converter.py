# this is a python program that takes weight as input and then converts it to either pounds or kilograms

print("Welcome!!!, How are you today")
print("Please enter your desired unit for your weight to be converted to, i.e pounds/ kilograms")

unit = input(" enter 'k' for kilo and l for pounds ")


if unit == "k" or unit == "K":
    weight = input("Enter your weight in pounds? ")

    conv_weight = float(weight) / 2.205
    print("Your weight in kilos is " + str(conv_weight))

elif unit == "l" or unit == "L":
    weight = input("Enter your weight in kilos? ")
    conv_weight = float(weight) * 2.205
    print("Your weight in pounds is " + str(conv_weight))

else:
    print("invalid input!!! ")



