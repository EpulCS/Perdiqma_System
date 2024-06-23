from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Perdiqma(models.Model):
       perdiqmaID = models.CharField(max_length=50,primary_key=True)
       perdiqmaname = models.CharField(max_length=100)
       perdiqmaphone = models.CharField(max_length=50)
       perdiqmapass = models.CharField(max_length=150)
       perdiqmabureau = models.CharField(max_length=150)

class Perdiqmaadmin(models.Model):
       adminID = models.CharField(max_length=50,primary_key=True)
       adminname = models.CharField(max_length=100)
       adminphone = models.CharField(max_length=50)
       adminpass = models.CharField(max_length=150)

class Activity(models.Model):
       title = models.CharField(max_length=200)
       description = models.TextField()
       date = models.DateField()
       members = models.ManyToManyField(Perdiqma, related_name='activities')
       created_by = models.ForeignKey(Perdiqmaadmin, on_delete=models.CASCADE)
       picture = models.ImageField(upload_to='activity_pictures/', blank=True, null=True)

       def __str__(self):
              return self.title

class GalleryPicture(models.Model):
       image = models.ImageField(upload_to='gallery_pictures/')
       caption = models.CharField(max_length=200)
       uploaded_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
              return self.caption
#class Activity(models.Model):
       #title = models.CharField(max_length=200)
       #description = models.TextField()
       #date = models.DateField()
       #members = models.ManyToManyField(Perdiqma, related_name='activities')
       #created_by = models.ForeignKey(Perdiqmaadmin, on_delete=models.CASCADE)

#class Gallery(models.Model):
      #image = models.ImageField(upload_to='gallery/')
      #description = models.TextField()
      #created_by = models.ForeignKey(Perdiqmaadmin, on_delete=models.CASCADE)












