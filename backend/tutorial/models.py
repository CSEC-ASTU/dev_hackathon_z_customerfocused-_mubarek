from django.db import models

# Create your models here.

class Tutorial(models.Model):
    image       = models.ImageField(upload_to="tutorial")
    name        = models.CharField(max_length=150)
    link        = models.CharField(max_length=500)
    description = models.TextField()

    def short_description(self):
        return self.description[:80]
    
    def __str__(self):
        return self.name