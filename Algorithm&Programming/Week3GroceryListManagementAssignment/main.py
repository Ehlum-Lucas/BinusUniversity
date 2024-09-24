def get_option():
    print("Choose an option:")
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Exit")
    return int(input("Enter your choice: "))

def main():
    items = []
    while True:
        option = get_option()
        if option == 1:
            items.append(input("Enter the item to add: "))
        elif option == 2:
            print("List of items:", items)
        elif option == 3:
            item = input("Enter the item to remove: ")
            if item in items:
                items.remove(item)
            else:
                print("Item not found")
        elif option == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
