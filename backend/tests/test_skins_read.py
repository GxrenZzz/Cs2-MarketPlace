from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_skins_query_params():

    # 1. Get all skins
    response = client.get("/skins")
    assert response.status_code == 200
    assert len(response.json()) == 6

    # 2. Filter by weapon
    response = client.get("/skins", params={"weapon": "AK-47"})
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert all(skin["weapon"] == "AK-47" for skin in response.json())

    # 3. Pagination using limit
    response = client.get("/skins", params={"limit": 2})
    assert response.status_code == 200
    assert len(response.json()) == 2

    # 4. Pagination using offset
    response = client.get("/skins", params={"limit": 2, "offset": 1})
    assert response.status_code == 200
    assert len(response.json()) == 2

    # 5. Invalid limit
    response = client.get("/skins", params={"limit": 0})
    assert response.status_code == 422

    # 6. Invalid offset
    response = client.get("/skins", params={"offset": -1})
    assert response.status_code == 422



def test_get_skin_by_id():

    # 1. Existing skin ID
    response = client.get("/skins/2")

    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["name"] == "Asiimov"

    # 2. Nonexistent skin ID
    response = client.get("/skins/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Skin Not Found"

    # 3. Invalid skin ID type
    response = client.get("/skins/abc")

    assert response.status_code == 422
