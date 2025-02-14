from rest_framework import serializers
from apps.quotes.models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Quote model.
    Transforms Quote instances into JSON and validates input data for API requests.
    """
    
    class Meta:
        model = Quote
        # fields = '__all__'
        fields = ["id", "author", "content", "timestamp"]