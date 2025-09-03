from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
#Navigate to bookshelf/models.py.
# Create a Book class with the following fields:
#title: CharField with a maximum length of 200 characters.
#author: CharField with a maximum length of 100 characters.
#publication_year: IntegerField.
#Ensure the model is correctly set up for migrations.

class Book(models.Model):
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    roles = [ 
        ('Admin', 'Admin'), 
        ('Librarian' , 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    role = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    

    

