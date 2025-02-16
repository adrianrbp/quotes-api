import pytest
from apps.quotes.tests.factories import QuoteFactory

@pytest.mark.django_db
class TestQuoteModel:
    def test_create_quote(self):
        """Ensure a Quote can be created successfully"""
        quote = QuoteFactory(author="John Doe", content="A great quote")
        assert quote.id is not None
        assert quote.author == "John Doe"
        assert quote.content == "A great quote"

    def test_quote_str_representation(self):
        """Ensure __str__ method returns expected format"""
        quote = QuoteFactory(author="Jane Doe", content="A wise saying")
        assert str(quote) == "A wise saying - Jane Doe"