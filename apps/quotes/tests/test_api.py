import pytest
from rest_framework import status

@pytest.mark.django_db
class TestQuoteAPI:
    def test_list_quotes(self, api_client):
        """Ensure we can retrieve a list of quotes"""
        response = api_client.get("/api/quotes/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data == []