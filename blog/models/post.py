from django.db import models
from .user import User
from .category import Category

# Create your models here.
# Models: Presenting the table structure in the database.
class Post(models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    # one-to-many relationship 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',null=True, blank=True)  # ForeignKey to User model
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)

    def __str__(self):
        return self.title