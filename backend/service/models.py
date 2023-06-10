from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Service(models.Model):
    icon            = models.ImageField(upload_to='service/icon')
    name            = models.CharField(max_length=150)
    description     = models.TextField()
    color_number    = models.IntegerField(
        validators=[ 
            MaxValueValidator(6),
            MinValueValidator(1)
        ])

    def short_description(self):
        return self.description[:100]

    def __str__(self):
        return self.name