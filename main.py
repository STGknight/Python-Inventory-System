inventory = {}

while True:
    print ("===Inventory Mangement System===")

    print("1. View Inventory")
    print("2. Add Item")
    print("3. Exit")

    choice = input("Chose an option :")

    if choice == "1":
        for item_name, item_info in inventory.items():
            print ("Item:", item_name)
            print("Quantity:", item_info["quantity"])
            print("Price: $", item_info["price"])
    elif choice == "2":
        item_name = input("Enter item name: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
    
        inventory[item_name]={
            "quantity": quantity,
            "price": price
        }

        print("Item added.")
        print(inventory)

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invail option")