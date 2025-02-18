import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from oauth2_provider.models import Application

@pytest.fixture
def api_client():
    """Fixture for API client"""
    return APIClient()

@pytest.fixture
def oauth_client(db, test_user):
    """Creates an OAuth2 application"""
    # test_client_id = "test-client-id"
    # test_client_secret = "test-client-secret"
    
    # return Application.objects.create(
    #     name="TestApp",
    #     client_type=Application.CLIENT_CONFIDENTIAL,
    #     authorization_grant_type=Application.GRANT_PASSWORD,
    #     user=test_user
    # )
    application = Application.objects.create(
        name="TestApp",
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
        user=test_user
    )
    
    # Store the plain-text secret before it is hashed
    application.raw_client_secret = "test-client-secret"
    
    # Manually set the client_secret to avoid hashing issues
    application.client_secret = application.raw_client_secret
    application.save()

    return application

@pytest.fixture
def test_user(db):
    """Creates a test user"""
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="password123")
