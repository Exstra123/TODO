from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=20, blank=False)
    author = models.CharField(max_length=20, blank=False)
    year = models.IntegerField(default=1900)

    def __str__(self):
        return f"{self.name}, {self.year} г."

class TODO(models.Model):
    text = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"