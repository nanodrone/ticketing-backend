def test_login_and_access_protected_route(client):
    user_response = client.post(
        "/users/",
        json={
            "name": "Denis",
            "email": "denis@example.com",
            "password": "Password123!"
        }
    )
    assert user_response.status_code == 200

    token_response = client.post(
        "/token",
        data={
            "username": "denis@example.com",
            "password": "Password123!"
        },
    )
    assert token_response.status_code == 200

    access_token = token_response.json()["access_token"]

    protected_response = client.get(
        "/tickets/",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert protected_response.status_code == 200