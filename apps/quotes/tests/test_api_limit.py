import pytest
from rest_framework import status

@pytest.mark.django_db
class TestQuoteAPILimit:
    def test_anon_rate_throttle(self, api_client):
        """Ensure anonymous users get throttled after exceeding the limit."""
        url = "/api/quotes/"  # Change this to your endpoint

        # Simulate 6 requests
        for _ in range(5):
            response = api_client.get(url)
            assert response.status_code == status.HTTP_200_OK  # Requests should succeed

        # 6th request should be throttled
        response = api_client.get(url)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS

    def test_user_rate_throttle(self, auth_client):
        """Ensure authenticated users get throttled after exceeding the limit."""
        url = "/api/quotes/"  # Change this to your endpoint

        # Simulate 21 requests
        for _ in range(20):
            response = auth_client.get(url)
            assert response.status_code == status.HTTP_200_OK  # Requests should succeed

        # 21st request should be throttled
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS
