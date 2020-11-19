from django.db import models


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    # TODO: def total_cards():
