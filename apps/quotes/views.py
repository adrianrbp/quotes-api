import random
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
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
        """
        Retrieve a random quote from the database.
        - Returns a 200 status code with a random quote if available.
        - Returns a 404 status code with an appropriate message if no quotes exist.
        """
        quotes = Quote.objects.all()

        if not quotes.exists():
            return Response(
                {
                    "status": 404,
                    "message": "No quotes available",
                    "data": None
                },
                status=status.HTTP_404_NOT_FOUND
            )

        random_quote = random.choice(quotes)
        serializer = self.get_serializer(random_quote)

        return Response(
            {
                "status": 200,
                "message": "Random quote retrieved successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )