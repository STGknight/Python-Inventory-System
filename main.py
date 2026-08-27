inventory = {}

while True:
    print ("===Inventory Mangement System===")

    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Exit")

    choice = input("Chose an option :")

    if choice == "1":
        for item_name, item_info in inventory.items():
            print ("Item:", item_name)
            print("Quantity:", item_info["quantity"])
            print("Price: $", item_info["price"])
    elif choice == "2":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    
        inventory[item_name]={
            "quantity": quantity,
            "price": price
        }

        print("Item added.")
        print(inventory)

    elif choice =="3":
        item_name = input("Enter item name to remove: ")

        if item_name in inventory:
            del inventory[item_name]
            print("item removed.")
        else:
            print("Item not found.")
    
    elif choice == "4":
        item_name = input("Enter item name to update: ")

        if item_name in inventory:
            print("Item found.")

            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new Price: "))

            inventory[item_name]["quantity"] = new_quantity 
            inventory[item_name]["price"] = new_price

            print("Item updated."
            )
        else:
            print("Item not found.")
        

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invail option")