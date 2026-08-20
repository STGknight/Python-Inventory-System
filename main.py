print ("===Inventory Mangement System===")

print("1. View Inventory")
print("2. Add Item")
print("3. Print")

choice = input("Chose an option :")

if choice == "1":
    print("Viewing Inventory")
elif choice == "2":
    print("Adding Item")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invail option")