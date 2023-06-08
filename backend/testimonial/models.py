from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Testimonials(models.Model):
    profile     = models.ImageField(upload_to="testimonial/profile")
    name        = models.CharField(max_length=150)
    relation    = models.CharField(max_length=150)
    rate        = models.IntegerField(
        validators=[ 
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    message     = models.TextField()

    def __str__(self):
        return self.name