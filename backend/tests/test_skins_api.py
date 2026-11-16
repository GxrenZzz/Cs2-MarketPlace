from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_create_skin():
    payload = {
        "name": "Dragon Lore",
        "weapon": "AWP",
        "rarity": "Covert",
        "wear": "Factory New",
        "min_float": 0.0,
        "max_float": 0.01,
        "price": 1000.0
    }

    response = client.post("/skins", json=payload)

    assert response.status_code == 201
    assert response.json()["name"] == "Dragon Lore"
    assert "id" in response.json()

def test_create_skin_invalid_float():
    payload = {
        "name": "Dragon Lore",
        "weapon": "AWP",
        "rarity": "Covert",
        "wear": "Factory New",
        "min_float": -0.1,
        "max_float": 0.5,
        "price": 1000.0
    }

    response = client.post("/skins", json=payload)

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert errors[0]["loc"] == ["body", "min_float"]