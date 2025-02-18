import pytest
from rest_framework import status
from apps.quotes.models import Quote
from apps.quotes.tests.factories import QuoteFactory

@pytest.mark.django_db
class TestQuoteAuthentication:
    
    def test_create_quote_requires_authentication(self, api_client):
        """Ensure an unauthenticated user cannot create a quote."""
        payload = {"author": "Test Author", "content": "Test Content"}
        response = api_client.post("/api/quotes/", payload)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_quote_requires_authentication(self, api_client, quote):
        """Ensure an unauthenticated user cannot update a quote."""
        updated_data = {"author": "Updated Author", "content": "Updated Content"}
        response = api_client.put(f"/api/quotes/{quote.id}/", updated_data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_quote_requires_authentication(self, api_client, quote):
        """Ensure an unauthenticated user cannot delete a quote."""
        response = api_client.delete(f"/api/quotes/{quote.id}/")

        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_authenticated_user_can_create_quote(self, auth_client):
        """Ensure an authenticated user can create a quote."""
        payload = {"author": "Authenticated Author", "content": "Authenticated Content"}
        response = auth_client.post("/api/quotes/", payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert Quote.objects.filter(author="Authenticated Author").exists()

    def test_authenticated_user_can_update_quote(self, auth_client, quote):
        """Ensure an authenticated user can update a quote."""
        updated_data = {"author": "Updated Author", "content": "Updated Content"}
        response = auth_client.put(f"/api/quotes/{quote.id}/", updated_data)

        assert response.status_code == status.HTTP_200_OK
        quote.refresh_from_db()
        assert quote.author == "Updated Author"
        assert quote.content == "Updated Content"

    def test_authenticated_user_can_delete_quote(self, auth_client, quote):
        """Ensure an authenticated user can delete a quote."""
        response = auth_client.delete(f"/api/quotes/{quote.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Quote.objects.filter(id=quote.id).exists()
