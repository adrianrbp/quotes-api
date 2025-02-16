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
    """
    queryset = Quote.objects.all().order_by('-timestamp')
    serializer_class = QuoteSerializer