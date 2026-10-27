from django.db import models

# Create your models here.
# Models: Presenting the table structure in the database.
class Post(models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    categories = models.ManyToManyField('Category', related_name='posts', blank=True)

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) # Same as in Post.

    def __str__(self):
        return self.username
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # Same as in Post and User

    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}: {self.content[:30]}"