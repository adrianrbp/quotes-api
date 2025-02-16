from django.core.management.base import BaseCommand
from apps.quotes.tests.factories import QuoteFactory
from apps.quotes.models import Quote

class Command(BaseCommand):
    help = "Seeds the database with sample quotes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=10,
            help="Number of quotes to generate",
        )

    def handle(self, *args, **options):
        count = options["count"]

        # Clear existing data (optional)
        Quote.objects.all().delete()

        self.stdout.write(self.style.WARNING(f"Seeding {count} quotes..."))
        for _ in range(count):
            QuoteFactory()

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} quotes!"))
