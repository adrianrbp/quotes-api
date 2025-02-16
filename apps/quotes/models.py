from django.db import models

class Quote(models.Model):
    """
    Represents a quote with text content, an author, and a timestamp.
    """
    id = models.AutoField(primary_key=True)
    content = models.TextField(help_text="The content of the quote.")
    author = models.CharField(max_length=255, help_text="The author of the quote.")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the quote was created.")

    def __str__(self):
        """
        Returns a string representation of the quote, showing the first 50 characters of content and the author.
        """
        return f"{self.content[:50]} - {self.author}"