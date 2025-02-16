import pytest
from apps.quotes.serializers import QuoteSerializer
from apps.quotes.models import Quote
from django.utils.timezone import now

@pytest.fixture
def quote():
    """Fixture to create a Quote instance (not saved to the DB)"""
    return Quote(
        author="Tesla",
        content="The present is theirs; the future, for which I really worked, is mine.",
        timestamp=now()
    )

def test_quote_serializer_serialization(quote):
    """Ensure QuoteSerializer correctly serializes a Quote instance"""
    serializer = QuoteSerializer(quote)
    expected_data = {
        "id": None,  # Not saved yet
        "author": quote.author,
        "content": quote.content,
        "timestamp": quote.timestamp.astimezone().isoformat(timespec="microseconds").replace("+00:00", "Z")
    }

    assert serializer.data == expected_data



def test_quote_serializer_deserialization():
    """Ensure QuoteSerializer correctly validates and deserializes input data"""
    data = {
        "author": "Curie",
        "content": "Nothing in life is to be feared, it is only to be understood."
    }
    serializer = QuoteSerializer(data=data)
    
    assert serializer.is_valid()
    assert serializer.validated_data["author"] == "Curie"
    assert serializer.validated_data["content"] == data["content"]
