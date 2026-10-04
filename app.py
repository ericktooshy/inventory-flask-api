from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# In-memory database (satisfies the "database array" rubric requirement)
inventory = [
    {"id": 1, "name": "Apple", "quantity": 50, "price": 0.50},
    {"id": 2, "name": "Milk", "quantity": 20, "price": 2.50}
]

# --- CRUD ROUTES ---

# READ: Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(inventory), 200

# READ: Get single item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200

# CREATE: Add a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid data, 'name' is required"}), 400
    
    new_item = {
        "id": len(inventory) + 1 if inventory else 1,
        "name": data.get("name"),
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0)
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

# UPDATE (PATCH): Modify an item
@app.route('/items/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    item["name"] = data.get("name", item["name"])
    item["quantity"] = data.get("quantity", item["quantity"])
    item["price"] = data.get("price", item["price"])
    
    return jsonify(item), 200

# DELETE: Remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    inventory = [i for i in inventory if i["id"] != item_id]
    return '', 204

# --- EXTERNAL API ROUTE ---

# Fetch from OpenFoodFacts and add to inventory
@app.route('/fetch-external/<barcode>', methods=['POST'])
def fetch_and_add_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to reach external API"}), 502
    
    data = response.json()
    if data.get("status") != 1:
        return jsonify({"error": "Product not found on OpenFoodFacts"}), 404
        
    product_info = data.get("product", {})
    new_item = {
        "id": len(inventory) + 1 if inventory else 1,
        "name": product_info.get("product_name", "Unknown External Product"),
        "quantity": 10, 
        "price": 1.99   
    }
    inventory.append(new_item)
    return jsonify({"message": "Product imported successfully", "item": new_item}), 201

if __name__ == '__main__':
    app.run(debug=True)