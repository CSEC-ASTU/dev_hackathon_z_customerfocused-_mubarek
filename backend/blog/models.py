from django.db import models

# Create your models here.
class Category(models.Model):
    title   = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Blog(models.Model):
    name        = models.CharField(max_length=250)
    image       = models.ImageField(upload_to="blog")
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def short_description(self):
        return self.description[:80]
    
    def __str__(self):
        return self.name
    