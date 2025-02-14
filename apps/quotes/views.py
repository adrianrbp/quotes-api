from rest_framework import generics
from apps.quotes.models import Quote
from apps.quotes.serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that allows quotes to be viewed.

    Endpoints:
    - GET /api/quotes/       -> Retrieve all quotes
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer