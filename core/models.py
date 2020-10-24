from django.db import models

# Create your models here.


class Country(models.Model):
    CATEGORY = [
        'ABC', 'DEF', 'GHI', 'JKL', 'MN', 'OPQ', 'RST', 'UVW', 'XYZ'
    ]
    name = models.CharField(max_length=50, unique=True)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.name
