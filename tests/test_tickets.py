def test_create_and_update_ticket(client):
    user_response = client.post(
        "/users/",
        json={"name": "Mario Rossi", "email": "mario@example.com"}
    )
    assert user_response.status_code == 200
    user_id = user_response.json()["id"]

    asset_response = client.post(
        "/assets/",
        json={
            "name": "Dell Latitude",
            "category": "laptop",
            "serial_number": "DL-TEST-001",
            "status": "available",
            "assigned_user_id": user_id
        }
    )
    assert asset_response.status_code == 200
    asset_id = asset_response.json()["id"]

    ticket_response = client.post(
        "/tickets/",
        json={
            "title": "Laptop non si avvia",
            "description": "Schermo nero dopo accensione",
            "priority": "medium",
            "user_id": user_id,
            "asset_id": asset_id
        }
    )
    assert ticket_response.status_code == 200
    ticket_id = ticket_response.json()["id"]

    patch_response = client.patch(
        f"/tickets/{ticket_id}",
        json={"status": "closed"}
    )
    assert patch_response.status_code == 200
    assert patch_response.json()["status"] == "closed"

def test_create_ticket_with_invalid_priority(client):
    user_response = client.post(
        "/users/",
        json={"name": "Luigi Bianchi", "email": "luigi@example.com"}
    )
    user_id = user_response.json()["id"]

    response = client.post(
        "/tickets/",
        json={
            "title": "Errore accesso",
            "description": "Non riesco ad accedere al portale",
            "priority": "urgentissimo",
            "user_id": user_id,
            "asset_id": None
        }
    )

    assert response.status_code == 422