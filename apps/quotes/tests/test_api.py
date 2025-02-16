import pytest
from rest_framework import status
from apps.quotes.models import Quote
from apps.quotes.tests.factories import QuoteFactory

@pytest.mark.django_db
class TestQuoteAPI:
    def test_list_quotes(self, api_client, quote):
        """Ensure we can retrieve a list of quotes"""
        response = api_client.get("/api/quotes/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]["content"] == quote.content
        assert response.data[0]["author"] == quote.author

    def test_create_quote(self, api_client):
        """Ensure we can create a new quote"""
        new_quote = QuoteFactory.build()
        new_quote_data = {
            "content": new_quote.content,
            "author": new_quote.author,
        }
        response = api_client.post("/api/quotes/", new_quote_data)
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Quote.objects.count() == 1
        assert Quote.objects.first().content == new_quote_data["content"]
        assert Quote.objects.first().author == new_quote_data["author"]