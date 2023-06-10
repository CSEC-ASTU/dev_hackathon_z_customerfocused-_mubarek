from django.db import models
from profiles.models import Profile

# Create your models here.

class Cv(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cv          = models.FileField(upload_to="cv")

    def __str__(self):
        return self.profile.first_name