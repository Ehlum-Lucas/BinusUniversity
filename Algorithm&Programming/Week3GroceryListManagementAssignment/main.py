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

"""
the main functions work well! just missing some error handling and input validation. this just means when the user inputs something they shouldnt be inputting (such as when the code asks for a number
but the user instead puts in a string), the code shouldnt just crash, but instead prints out an error message. same with input validation, the code should let the user know that their input has been
accepted and give appropriate feedback like "Item added successfully!", something like that. but overall i think the code is great!
"""
