class Canteen:
    def __init__(self, input_option: int):
        assert input_option >= 0, f"{input_option} you have entered a wrong input. Next person please!."
        self.input_option = input_option

        # declaration of dictionaries
        self.food_item = {"Rice": 200, "Beans": 300, "Yam": 500, "Spaghetti": 100}
        self.addon = {"Meat": 1000, "Egg": 150, "Chicken": 2000, "Fish": 500}
        self.drinks = {"Malt": 500, "Bottled Water": 200, "Pepsi": 300, "Coke": 300}

    def purchase_food_with_numbers(self):
        customer_order = {}
        #print out foods in the dictionary
        i = 1
        for index in self.food_item:
            print(f"{i} for {index}")
            i += 1
        food_choice = int(
            input("Please check what we have and make a choice from the options available" + "\U0001F642"))
            #code block to handle selection of rice
        if food_choice == 1:
            print("You have chosen rice")
            customer_order["Rice"] = self.food_item["Rice"]

            portions = int(input("How many portions do you want ?...."))
            customer_order.update({"portions": portions})
            food_amount = customer_order.get("Rice") * portions
            customer_order.update({"total food price": food_amount})

            # code block to handle selection of drinks
            drink_choice = input("Order taken! \n Would you like a drink with that? ")
            if drink_choice == "yes" or drink_choice == "Yes":
                i = 1
                for index in self.drinks:
                    print(f"{i} for {index}")
                    i += 1
                drink_choice = int(input("Please select a drink.... "))
                # first drink
                if drink_choice == 1:
                    customer_order["Malt"] = self.drinks["Malt"]
                    portions = int(input("How many cans/bottles do you want ?...."))
                    customer_order.update({"portions": portions})
                    drinks_amount = customer_order.get("Malt") * portions
                    customer_order["total drinks price"] = drinks_amount
                # second drink
                elif drink_choice == 2:
                    customer_order["Bottled Water"] = self.drinks["Bottled Water"]
                    portions = int(input("How many cans/bottles do you want ?...."))
                    customer_order.update({"portions": portions})
                    drinks_amount = customer_order.get("Bottled Water") * portions
                    customer_order["total drinks price"] = drinks_amount
                # third drink
                elif drink_choice == 3:
                    customer_order["Pepsi"] = self.drinks["Pepsi"]
                    portions = int(input("How many cans/bottles do you want ?...."))
                    customer_order.update({"portions": portions})
                    drinks_amount = customer_order.get("Pepsi") * portions
                    customer_order["total drinks price"] = drinks_amount
                # fourth drink
                elif drink_choice == 4:
                    customer_order["Coke"] = self.drinks["Coke"]
                    portions = int(input("How many cans/bottles do you want ?...."))
                    customer_order.update({"portions": portions})
                    drinks_amount = customer_order.get("Coke") * portions
                    customer_order["total drinks price"] = drinks_amount

            elif drink_choice == "no" or drink_choice == "No":
                addon_choice = int(input("Would you like a protein addon instead?... "))
                # code block to handle protein selection
                if addon_choice == "yes" or drink_choice == "Yes":
                    i = 1
                    for index in self.addon:
                        print(f"{i} for {index}")
                        i += 1
                    addon_choice = int(input("Please select a protein addon .... "))
                    # first drink
                    if addon_choice == 1:
                        customer_order["Meat"] = self.drinks["Meat"]
                        portions = int(input("How many pieces do you want ?...."))
                        customer_order.update({"portions": portions})
                        addon_amount = customer_order.get("Meat") * portions
                        customer_order["total protein addon price"] = addon_amount
                    # second drink
                    elif addon_choice == 2:
                        customer_order["Meat"] = self.drinks["Meat"]
                        portions = int(input("How many pieces do you want ?...."))
                        customer_order.update({"portions": portions})
                        addon_amount = customer_order.get("Meat") * portions
                        customer_order["total protein addon price"] = addon_amount
                    # third drink
                    elif addon_choice == 3:
                        customer_order["Meat"] = self.drinks["Meat"]
                        portions = int(input("How many pieces do you want ?...."))
                        customer_order.update({"portions": portions})
                        addon_amount = customer_order.get("Meat") * portions
                        customer_order["total protein addon price"] = addon_amount
                    # fourth drink
                    elif addon_choice == 4:
                        customer_order["Meat"] = self.drinks["Meat"]
                        portions = int(input("How many pieces do you want ?...."))
                        customer_order.update({"portions": portions})
                        addon_amount = customer_order.get("Meat") * portions
                        customer_order["total protein addon price"] = addon_amount

        for item in customer_order:
            print(item, customer_order[item])




        if food_choice == 2:
            print("You have chosen Beans")
            customer_order["Beans"] = self.food_item["Beans"]

            portions = int(input("How many portions do you want ?...."))
            customer_order.update({"portions": portions})
            total_amount = customer_order.get("Beans") * portions
            customer_order["total amount"] = total_amount

            for item in customer_order:
                print(item, customer_order[item])

        if food_choice == 3:
            print("You have chosen yam")
            customer_order["Yam"] = self.food_item["Yam"]

            portions = int(input("How many portions do you want ?...."))
            customer_order.update({"portions": portions})
            total_amount = customer_order.get("Yam") * portions
            customer_order.update({"total amount": total_amount})

            for item in customer_order:
                print(item, customer_order[item])

        if food_choice == 4:
            print("You have chosen spaghetti")
            customer_order["Spaghetti"] = self.food_item["Spaghetti"]

            portions = int(input("How many portions do you want ?...."))
            customer_order.update({"portions": portions})
            total_amount = customer_order.get("Spaghetti") * portions
            customer_order.update({"total amount": total_amount})






print("Welcome to our canteen!")
input_option = int(input("Please select an input method for your orders.....\n 1 for numbers........\n 2 for keywords"))
canteen = Canteen(input_option)

if input_option == 1:
    print("You have chosen your input method")

    canteen.purchase_food_with_numbers()
