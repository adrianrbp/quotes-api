import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.quotes.tests.factories import QuoteFactory

@pytest.fixture
def api_client():
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
def auth_client(api_client, user):
    """Authenticates the client with the test user"""
    api_client.force_authenticate(user=user)
    return api_client