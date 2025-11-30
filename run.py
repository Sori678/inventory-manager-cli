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
def add_product(inventory):
    """
    Add a new product to the inventory with validated input.
    """
    print("\n=== Add New Product ===")
    name = input("Product name: ").strip()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        quantity = int(input("Quantity (integer): ").strip())
        price = float(input("Price (use . for decimals): ").strip())
    except ValueError:
        print("Invalid input! Quantity must be an integer and price must be a number.")
        return

    if quantity < 0 or price < 0:
        print("Quantity and price must be positive values.")
        return

    # Generate a new ID
    if inventory:
        new_id = max(item["id"] for item in inventory) + 1
    else:
        new_id = 1

    new_product = {
        "id": new_id,
        "name": name,
        "quantity": quantity,
        "price": price,
    }

    inventory.append(new_product)
    print(f"Product '{name}' added successfully with ID {new_id}!")
def update_product(inventory):
    """
    Update quantity and/or price for an existing product.
    """
    if not inventory:
        print("\nInventory is empty. Nothing to update.")
        return

    print("\n=== Update Product ===")
    try:
        product_id = int(input("Enter product ID to update: ").strip())
    except ValueError:
        print("Invalid ID! ID must be an integer.")
        return

    # Search for the product
    product = next((item for item in inventory if item["id"] == product_id), None)

    if not product:
        print(f"No product found with ID {product_id}.")
        return

    print(f"Current product: {product['name']} | "
          f"Quantity: {product['quantity']} | Price: €{product['price']}")

    # New quantity if the user wants
    new_quantity_input = input(
        "New quantity (leave blank to keep current): "
    ).strip()

   # New price if the user wants
    new_price_input = input(
        "New price (leave blank to keep current): "
    ).strip()

    try:
        if new_quantity_input:
            new_quantity = int(new_quantity_input)
            if new_quantity < 0:
                print("Quantity must be positive.")
                return
            product["quantity"] = new_quantity

        if new_price_input:
            new_price = float(new_price_input)
            if new_price < 0:
                print("Price must be positive.")
                return
            product["price"] = new_price

        print("Product updated successfully!")

    except ValueError:
        print("Invalid value! Quantity must be integer and price must be a number.")
def delete_product(inventory):
    """
    Delete a product from the inventory by its ID.
    """
    if not inventory:
        print("\nInventory is empty. Nothing to delete.")
        return

    print("\n=== Delete Product ===")
    try:
        product_id = int(input("Enter product ID to delete: ").strip())
    except ValueError:
        print("Invalid ID! ID must be an integer.")
        return

    # Search for the product
    product = next((item for item in inventory if item["id"] == product_id), None)

    if not product:
        print(f"No product found with ID {product_id}.")
        return

    print(f"You are about to delete: {product['name']} "
          f"(Qty: {product['quantity']}, Price: €{product['price']})")
    confirm = input("Are you sure? (y/n): ").strip().lower()

    if confirm == "y":
        inventory.remove(product)
        print("Product deleted successfully!")
    else:
        print("Delete cancelled.")

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
            add_product(inventory)
        elif choice == "3":
            update_product(inventory)
        elif choice == "4":
            delete_product(inventory)
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

