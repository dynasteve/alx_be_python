shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    if item in shopping_list:
      shopping_list.remove(item)
      return "Success"
    else:
        return "Item not in list"

def display_list():
    for item in shopping_list:
        print(f"{item}")

def main():
    global shopping_list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)

        elif choice == '2':
            item = input("Enter the item to remove: ")
            print(remove_item(item))
            
        elif choice == '3':
            display_list()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()