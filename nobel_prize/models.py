from django.db import models

class NobelPrize(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.year}"