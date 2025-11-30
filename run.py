import json

# Load data from JSON file
def load_data():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database not found, creating a new one...")
        return []
    except json.JSONDecodeError:
        print("Error reading database file. Starting with empty data.")
        return []

# Save data to JSON file
def save_data(data):
    try:
        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Database saved successfully!")
    except Exception as e:
        print(f"Error saving database: {e}")
def show_menu():
    """
    Display the main menu options for the inventory manager.
    """
    print("\n=== Inventory Manager ===")
    print("1. Show inventory")
    print("2. Add product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Search product")
    print("6. Save and exit")
def show_inventory(inventory):
    """
    Display all products in the inventory in a formatted way.
    """
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\n=== Current Inventory ===")
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | "
            f"Quantity: {item['quantity']} | Price: €{item['price']}"
        )

def main():
    inventory = load_data()

    print("Welcome to Inventory Manager CLI!")
    print(f"Loaded {len(inventory)} products from database.")

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            print("TODO: Add product")
        elif choice == "3":
            print("TODO: Update product")
        elif choice == "4":
            print("TODO: Delete product")
        elif choice == "5":
            print("TODO: Search product")
        elif choice == "6":
            save_data(inventory)
            print("Database saved. Goodbye!")
            break
        else:
            print("Invalid option, please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()

