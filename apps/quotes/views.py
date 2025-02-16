from rest_framework import generics
from apps.quotes.models import Quote
from apps.quotes.serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows quotes to be viewed.

    Endpoints:
    - GET /api/quotes/       -> Retrieve all quotes
    - POST /api/quotes/      -> Create a new quote
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer