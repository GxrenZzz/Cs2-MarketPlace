from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
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



# tests/test_skins_api.py

# Sample request body
skin_payload = {
    "name": "Redline",
    "weapon": "AK-47",
    "rarity": "Classified",
    "wear": "Field-Tested",
    "min_float": 0.1,
    "max_float": 0.3,
    "price": 25.5
}


def test_create_skin(client):
    response = client.post("/skins", json=skin_payload)

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Redline"
    assert data["weapon"] == "AK-47"


def test_get_all_skins(client):
    # First create a skin
    client.post("/skins", json=skin_payload)

    response = client.get("/skins")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["name"] == "Redline"


def test_get_skin_by_id(client):
    # Create a skin
    client.post("/skins", json=skin_payload)

    response = client.get("/skins/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Redline"
    


def test_update_skin(client):
    # Create a skin
    client.post("/skins", json=skin_payload)

    updated_payload = {
        "name": "Redline Updated",
        "weapon": "AK-47",
        "rarity": "Classified",
        "wear": "Factory New",
        "min_float": 0.01,
        "max_float": 0.07,
        "price": 100.0
    }

    response = client.put("/skins/1", json=updated_payload)

    assert response.status_code == 200
    assert response.json()["name"] == "Redline Updated"
    assert response.json()["price"] == 100.0


def test_delete_skin(client):
    # Create a skin
    client.post("/skins", json=skin_payload)

    response = client.delete("/skins/1")

    assert response.status_code == 204
    assert response.content == b""

    # Verify that the skin was deleted
    get_response = client.get("/skins/1")

    assert get_response.status_code == 404
    assert get_response.json() == {
    "message": "Skin Not Found",
    "code": 404,
    "details": "Skin not present in the exisiting Repository"
}


# Missing resource tests

def test_get_nonexistent_skin(client):
    response = client.get("/skins/999")

    assert response.status_code == 404
    assert response.json() == {
    "message": "Skin Not Found",
    "code": 404,
    "details": "Skin not present in the exisiting Repository"
}


def test_update_nonexistent_skin(client):
    response = client.put("/skins/999", json=skin_payload)

    assert response.status_code == 404
    assert response.json() == {
    "message": "Skin Not Found",
    "code": 404,
    "details": "Skin not present in the exisiting Repository"
}


def test_delete_nonexistent_skin(client):
    response = client.delete("/skins/999")

    assert response.status_code == 404
    assert response.json() == {
    "message": "Skin Not Found",
    "code": 404,
    "details": "Skin not present in the exisiting Repository"
}
def test_repository_isolation(client):
    response = client.get("/skins")

    assert response.status_code == 200
    assert response.json() == []