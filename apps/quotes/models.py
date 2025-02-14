from django.db import models

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    author = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content[:50]} - {self.author}"