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

    def test_retrieve_quote(self, api_client, quote):
        """Ensure we can retrieve a single quote by ID"""
        response = api_client.get(f"/api/quotes/{quote.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["content"] == quote.content

    def test_update_quote(self, api_client, quote):
        """Ensure we can update a quote"""
        updated_data = {"author": "Updated Author", "content": "Updated Text"}
        response = api_client.put(f"/api/quotes/{quote.id}/", updated_data)

        assert response.status_code == status.HTTP_200_OK
        quote.refresh_from_db()
        assert quote.author == "Updated Author"

    def test_delete_quote(self, api_client, quote):
        """Ensure we can delete a quote"""
        response = api_client.delete(f"/api/quotes/{quote.id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Quote.objects.count() == 0

    def test_get_random_quote(self, api_client):
        """Ensure we can retrieve a random quote"""
        QuoteFactory.create_batch(5)

        response = api_client.get(f"/api/quotes/random/")

        assert response.status_code == status.HTTP_200_OK
        assert "author" in response.json()
        assert "content" in response.json()

    def test_random_quote_no_quotes(self, api_client):
        """Ensure the API returns 'No quotes available' when no quotes exist."""
        response = api_client.get(f"/api/quotes/random/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["error"] == "No quotes available"