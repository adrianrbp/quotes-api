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