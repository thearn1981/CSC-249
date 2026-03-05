def menu():
    '''Displays the inventory menu.'''
    print("-" * 8 + "Inventory Menu" + "-" * 8)
    print("1) View Inventory") 
    print("2) Search Inventory")
    print("3) Exit")
    print("-" * 30) 

def main():
    '''Main function to run the inventory menu.'''
    inventory = ["Rusty Sword", "Gold Key", "Healing Apple", "Mystery Potion", "Torch"]

    while True:
        menu()
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            print("Viewing Inventory!")
            for item in inventory:
                print(f"- {item}")

        elif choice == '2':
            print("Searching Inventory...")
            try:
                search_item = input("Enter the item to search for: ").lower()
                found = False
                for index, item in enumerate(inventory):
                    if item.lower() == search_item:
                        print(f"Item: {search_item} found at index {index}.")
                        found = True
                        break
                if not found:
                    print(f"{search_item} is not in the inventory.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()