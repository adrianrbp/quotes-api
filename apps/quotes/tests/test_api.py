import pytest
from rest_framework import status

@pytest.mark.django_db
class TestQuoteAPI:
    def test_list_quotes(self, api_client, quote):
        """Ensure we can retrieve a list of quotes"""
        response = api_client.get("/api/quotes/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["content"] == quote.content
        assert response.data[0]["author"] == quote.author