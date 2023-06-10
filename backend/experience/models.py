from django.db import models

# Create your models here.

class Work(models.Model):
    company     = models.CharField(max_length=150)
    title       = models.CharField(max_length=150)
    description = models.TextField()
    start       = models.IntegerField()
    to          = models.CharField(max_length=50)

    def short_description(self):
        return self.description[:50]
    
    def __str__(self):
        return self.title

class Education(models.Model):
    institute   = models.CharField(max_length=150)
    title       = models.CharField(max_length=150)
    description = models.TextField()
    start       = models.IntegerField()
    to          = models.IntegerField()

    def short_description(self):
        return self.description[:50]
    
    def __str__(self):
        return self.title

