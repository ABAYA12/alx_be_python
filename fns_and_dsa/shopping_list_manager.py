shopping_list = []


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def shopping():
    try:
        while True:
            display_menu()
            choice = input('Enter your choice: ')
            if choice.isdigit():  # Ensure it's a number before converting
                choice = int(choice)
                if choice == 1:
                    item_name = input('Enter name of item: ').title()
                    shopping_list.append(item_name)
                elif choice == 2:
                    remove_item_name = input(
                        'Enter name of item you want to remove: ').title()
                    if remove_item_name in shopping_list:
                        shopping_list.remove(remove_item_name)
                    else:
                        print(
                            'Item not found. Please check the name of the item or try again.')
                elif choice == 3:
                    if shopping_list:
                        print("Available Items in Shop Now:")
                        for item in shopping_list:
                            print(item)
                    else:
                        print("Your shopping list is empty.")
                elif choice == 4:
                    print('Goodbye!')
                    break
                else:
                    print("Invalid choice, please try again.")
            else:
                print("Please enter a valid number.")
    except Exception as e:
        print(f"Error! : {e}")


shopping()
