from rest_framework import serializers
from apps.quotes.models import Quote

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        # fields = '__all__'
        fields = ["id", "author", "content", "timestamp"]