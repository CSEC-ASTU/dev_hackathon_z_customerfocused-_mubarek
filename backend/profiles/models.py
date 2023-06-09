from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name          = models.CharField(max_length=150)
    last_name           = models.CharField(max_length=150)
    email               = models.EmailField(max_length=354)
    address             = models.CharField(max_length=150)
    image               = models.ImageField(upload_to='profile')
    cover_image         = models.ImageField(upload_to='cover')
    phone               = models.CharField(max_length=50)
    age                 = models.IntegerField()
    nationality         = models.CharField(max_length=150)
    language            = models.CharField(max_length=550)
    work_experience     = models.IntegerField()
    popup_image1        = models.ImageField(upload_to='popup')
    popup_image2        = models.ImageField(upload_to='popup')
    short_description   = models.CharField(max_length=500)
    description         = models.TextField()
    completed_projects  = models.IntegerField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class SocialAccount(models.Model):
    profile     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    socialmedia = models.CharField(max_length=150)
    link        = models.CharField(max_length=350)

    def __str__(self):
        return self.socialmedia
    
    