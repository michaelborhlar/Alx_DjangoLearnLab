from django.db import models

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
        ('Admin', 'Admin') 
        ('Librarian' , 'Librarian')
        ('Member', 'Member')
    ]
    user = models.OneToOneField(User, on_delete= "CASCADE", related_name="user")
    role = models.CharField(max_length=50, choices=roles)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

