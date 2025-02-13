from rest_framework import generics
from rest_framework.response import Response

class QuoteListCreateView(generics.GenericAPIView):
    def get(self, request):
        return Response([])