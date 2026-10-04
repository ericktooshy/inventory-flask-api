import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

def view_all():
    response = requests.get(f"{BASE_URL}/items")
    if response.status_code == 200:
        print("\n--- Current Inventory ---")
        for item in response.json():
            print(f"ID: {item['id']} | Name: {item['name']} | Qty: {item['quantity']} | Price: ${item['price']}")
    else:
        print("Error fetching items.")

def add_item():
    name = input("Enter product name: ")
    quantity = input("Enter quantity: ")
    price = input("Enter price: ")
    
    payload = {"name": name, "quantity": int(quantity), "price": float(price)}
    response = requests.post(f"{BASE_URL}/items", json=payload)
    if response.status_code == 201:
        print(f"Successfully added: {response.json()['name']}")
    else:
        print("Failed to add item.")

def fetch_external():
    barcode = input("Enter OpenFoodFacts barcode (e.g., 737628064502): ")
    print("Fetching data...")
    response = requests.post(f"{BASE_URL}/fetch-external/{barcode}")
    
    if response.status_code == 201:
        print(f"Success! Added: {response.json()['item']['name']}")
    else:
        print(f"Error: {response.json().get('error', 'Could not fetch product')}")

def main_menu():
    while True:
        print("\n===== Inventory Management =====")
        print("1. View all items")
        print("2. Add a new item")
        print("3. Find a product on OpenFoodFacts")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            view_all()
        elif choice == '2':
            add_item()
        elif choice == '3':
            fetch_external()
        elif choice == '4':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()