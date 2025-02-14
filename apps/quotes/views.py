from rest_framework import generics
from apps.quotes.models import Quote
from apps.quotes.serializers import QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer