import pytest

@pytest.mark.django_db
class TestUserAuthentication:
    def test_register_user(self, api_client):
        """Test user registration"""
        data = {"username": "testuser", "password": "password123", "email": "test@example.com"}
        response = api_client.post("/api/users/register/", data, format="json")

        assert response.status_code == 201
        assert response.data["status"] == "success"
        assert "data" in response.data
        assert "message" in response.data
        assert response.data["data"]["username"] == "testuser"

    def test_register_existing_user(self, api_client, test_user):
        """Test registering an already existing user"""
        data = {
            "username": test_user.username,
            "email": test_user.email,
            "password": "password123",
        }
        response = api_client.post("/api/users/register/", data, format="json")

        assert response.status_code == 400
        assert response.data["status"] == "error"
        assert response.data["message"] == "Validation error"

    def test_login_oauth(self, api_client, oauth_client, test_user):
        """Test obtaining an access token using OAuth2 password grant"""
        test_user.set_password("password123")
        test_user.save()

        response = api_client.post("/api/oauth/token/", data={
            "grant_type": "password",
            "username": test_user.username,
            "password": "password123",
            "client_id": oauth_client.client_id,
            "client_secret": oauth_client.raw_client_secret,
        })
        
        assert response.status_code == 200
        json_data = response.json()
        assert "access_token" in json_data
        assert "refresh_token" in json_data
        assert json_data["token_type"] == "Bearer"