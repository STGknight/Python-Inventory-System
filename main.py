inventory = {}

print ("===Inventory Mangement System===")

print("1. View Inventory")
print("2. Add Item")
print("3. Exit")

choice = input("Chose an option :")

if choice == "1":
    print(inventory)
elif choice == "2":
    item_name = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    
    inventory[item_name]={
        "quantity": quantity
        "price": price
    }

    print("Item added.")
    print(inventory)

elif choice == "3":
    print("Goodbye!")
else:
    print("Invail option")