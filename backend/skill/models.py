from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Skill(models.Model):
    icon    = models.ImageField(upload_to="skill/icon")
    title   = models.CharField(max_length=150)
    percent = models.IntegerField(
        validators=[ 
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    
    def __str__(self):
        return self.title
    