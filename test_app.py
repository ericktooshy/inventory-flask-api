import pytest
from app import app, inventory

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Reset inventory state before each test
        inventory.clear()
        inventory.append({"id": 1, "name": "Test Item", "quantity": 10, "price": 1.00})
        yield client

def test_get_items(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Test Item"

def test_create_item(client):
    response = client.post('/items', json={"name": "New Apple", "quantity": 30, "price": 0.75})
    assert response.status_code == 201
    assert response.json["name"] == "New Apple"

def test_update_item(client):
    response = client.patch('/items/1', json={"quantity": 15})
    assert response.status_code == 200
    assert response.json["quantity"] == 15

def test_delete_item(client):
    response = client.delete('/items/1')
    assert response.status_code == 204