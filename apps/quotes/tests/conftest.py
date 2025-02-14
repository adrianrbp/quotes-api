import pytest
from rest_framework.test import APIClient
from apps.quotes.models import Quote

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def quote(db):
    """Creates a test quote"""
    return Quote.objects.create(
            content="The only limit to our realization of tomorrow is our doubts of today.",
            author="Franklin D. Roosevelt"
        )