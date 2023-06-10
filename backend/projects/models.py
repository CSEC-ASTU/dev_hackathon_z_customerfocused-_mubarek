from django.db import models

# Create your models here.

class Category(models.Model):
    title   = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
    

class Project(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    language    = models.CharField(max_length=150)
    client      = models.CharField(max_length=150)
    link        = models.CharField(max_length=500)
    title       = models.CharField(max_length=150) 
    description = models.TextField()
    image       = models.ImageField(upload_to="projects")

    def short_description(self):
        return self.description[:50]
    
    def __str__(self):
        return self.title