import factory
from apps.quotes.models import Quote

class QuoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quote

    author = factory.Faker("name")
    content = factory.Faker("sentence")