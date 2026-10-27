from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Same as in Post and User
        
    def __str__(self):
        return self.name