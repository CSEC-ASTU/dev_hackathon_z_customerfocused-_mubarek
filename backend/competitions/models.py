from django.db import models

# Create your models here.

class Competitions(models.Model):
    image       = models.ImageField(upload_to="competitions")
    name        = models.CharField(max_length=150)
    year        = models.IntegerField()
    description = models.TextField()

    def short_description(self):
        return self.description[:80]
    
    def __str__(self):
        return self.name