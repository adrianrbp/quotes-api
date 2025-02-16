import random
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from apps.quotes.models import Quote
from apps.quotes.serializers import QuoteSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quotes to be viewed.

    Endpoints:
    - GET /api/quotes/       -> Retrieve all quotes
    - POST /api/quotes/      -> Create a new quote
    - GET /api/quotes/{id}/  -> Retrieve a specific quote
    - PUT /api/quotes/{id}/  -> Update a quote
    - DELETE /api/quotes/{id}/ -> Delete a quote
    """
    queryset = Quote.objects.all().order_by('-timestamp')
    serializer_class = QuoteSerializer

    @action(detail=False, methods=["get"], url_path="random")
    def random_quote(self, request):
        """Retrieve a random quote"""
        quote = random.choice(Quote.objects.all()) if Quote.objects.exists() else None
        if quote:
            return Response(QuoteSerializer(quote).data)
        return Response({"error": "No quotes available"}, status=404)