import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.core.cache import cache
from apps.quotes.tests.factories import QuoteFactory
from oauth2_provider.models import Application

@pytest.fixture
def api_client():
    """Fixture for API client"""
    return APIClient()

@pytest.fixture
def quote(db):
    """Creates a test quote"""
    return QuoteFactory()

@pytest.fixture
def user(db):
    """Creates a test user"""
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="password")

@pytest.fixture
def oauth_client(db, user):
    """Creates an OAuth2 application"""
    application = Application.objects.create(
        name="TestApp",
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
        user=user
    )
    
    # Store the plain-text secret before it is hashed
    application.raw_client_secret = "test-client-secret"
    
    # Manually set the client_secret to avoid hashing issues
    application.client_secret = application.raw_client_secret
    application.save()

    return application

@pytest.fixture
def access_token(db, api_client, user, oauth_client):
    """Obtains an OAuth2 access token for the test user"""
    response = api_client.post(
        "/api/oauth/token/", 
        data={
            "grant_type": "password",
            "username": user.username,
            "password": "password",
            "client_id": oauth_client.client_id,
            "client_secret": oauth_client.raw_client_secret
        }
    )
    json_data = response.json()
    return json_data["access_token"]

@pytest.fixture
def auth_client(api_client, access_token):
    """Authenticates the client with the OAuth2 access token"""
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    return api_client

@pytest.fixture(autouse=True)
def clear_cache():
    """Clears the cache before each test to reset throttling."""
    cache.clear()