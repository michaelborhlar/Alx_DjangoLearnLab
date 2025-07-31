from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#In your Django project, you will extend the Django User model to include user roles 
# and develop views that restrict access based on these roles. Your task is
#  to set up this system by creating a new model for user profiles, defining views 
# with access restrictions, and configuring URL patterns.

#Step 1: Extend the User Model with a UserProfile
#Create a UserProfile model that includes a role field with predefined roles. 
# This model should be linked to Django’s built-in User model with a one-to-one relationship.

#Fields Required:
#user: OneToOneField linked to Django’s User.
#role: CharField with choices for ‘Admin’, ‘Librarian’, and ‘Member’.
#Automatic Creation: Use Django signals to automatically create a UserProfile when a new user is registered.

class UserProfile(models.Model):
    ROLE_CHOICES = [
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name="books", 
                               null=True, blank = True)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name= "library")


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete= models.CASCADE, null = True, blank=True)

    

    def __str__(self):
        return self.name
