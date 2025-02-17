import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from oauth2_provider.models import Application

@pytest.fixture
def api_client():
    """Fixture for API client"""
    return APIClient()

@pytest.fixture
def test_application(db):
    """Fixture to create an OAuth2 Application"""
    return Application.objects.create(
        name="TestApp",
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
        client_id="test_client_id",
        client_secret="test_client_secret"
    )

@pytest.fixture
def test_user(db):
    """Creates a test user"""
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="password123")
