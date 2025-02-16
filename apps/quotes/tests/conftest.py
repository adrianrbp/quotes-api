import pytest
from rest_framework.test import APIClient
from apps.quotes.tests.factories import QuoteFactory

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def quote(db):
    """Creates a test quote"""
    return QuoteFactory()