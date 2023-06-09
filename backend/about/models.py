from django.db import models
from profiles.models import Profile

# Create your models here.

class About(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    about       = models.TextField()

    def __str__(self):
        return self.about[:150]