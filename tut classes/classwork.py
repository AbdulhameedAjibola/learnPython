print("Good day! welcome to our canteen ")
customer_order = {}
food = {"Rice": 200, "Beans": 300, "Yam": 500, "Spaghetti": 100}
protein = {"Meat": 1000, "Egg": 150, "Chicken": 2000, "Fish": 500}
drinks = {"Malt": 500, "Bottled Water": 200, "Pepsi": 300, "Coke": 300}

#foods we have
print("Welcome to our canteen!.............................")
option = int(input("Please select a mode a input\n 1 for Item Names \n 2 for Item number... "))
if option == 1:
    print("We have: ")
    for item in food:
        print(item, food[item])
    food_choice = input("What would you like to have? ")

    if food_choice.capitalize() in food:
        print("Order taken")
        customer_order = {"food": food_choice}
    else:
        print("Invalid input")

    # proteins we have
    for item in protein:
        print(item, protein[item])
    protein_choice = input("What would you want on it? ")

    if protein_choice.capitalize() in protein:
        print("Order taken")
        customer_order.update({"protein": protein_choice})
    else:
        print("Invalid input")

    # drinks we have
    print("Would you like a drink with that ?")
    for item in drinks:
        print(item, drinks[item])
    drink_choice = input("What would you want on it? ")

    if drink_choice.capitalize() in drinks:
        print("Order taken")
        customer_order.update({"drink": drink_choice})
    else:
        print("Invalid input")

    print("Please confirm your order: ")
    for order in customer_order:
        print(customer_order[order])


