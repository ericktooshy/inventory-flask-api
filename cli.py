import requests
import sys

BASE_URL = "http://127.0.0.1:5000/items"

def list_items():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("\n--- Current Inventory ---")
        for item in response.json():
            print(f"ID: {item['id']} | Name: {item['name']} | Qty: {item['quantity']} | Price: ${item['price']}")
    else:
        print("Error fetching items.")

def add_item(name, quantity, price):
    payload = {"name": name, "quantity": int(quantity), "price": float(price)}
    response = requests.post(BASE_URL, json=payload)
    if response.status_code == 201:
        print(f"Successfully added: {response.json()['name']}")
    else:
        print("Failed to add item.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py [list | add <name> <qty> <price>]")
    else:
        command = sys.argv[1]
        if command == "list":
            list_items()
        elif command == "add" and len(sys.argv) == 5:
            add_item(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("Invalid command or arguments.")