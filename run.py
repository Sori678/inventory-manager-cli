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

def main():
    inventory = load_data()

    print("Welcome to Inventory Manager CLI!")
    print(f"Loaded {len(inventory)} products from database.")

    # Test saving the DB
    save_data(inventory)

if __name__ == "__main__":
    main()
