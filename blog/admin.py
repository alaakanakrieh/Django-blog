from atexit import register

from django.contrib import admin

from blog.models.user import User

from .models import Post, Category, Comment

# this is the default way to register models in the admin dashboard 
#admin.site.register(Post)

# Custumizations for the admin dashboard
# this method is used by the programmers.
@admin.register(Post) # this called admin decorator, it is used to register the model with the admin site
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id','title', 'author')
    list_filter = ('title_id','title', 'author')
    search_fields = ('title_id','title', 'author')
    ordering = ('title_id','title', 'author')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at')
    list_filter = ('username', 'email', 'first_name', 'last_name', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username', 'email', 'first_name', 'last_name')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name', 'description')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'author', 'created_at', 'updated_at')
    list_filter = ('content', 'post', 'author', 'created_at', 'updated_at')
    search_fields = ('content', 'post__title', 'author__username')
    ordering = ('created_at',)
    
#admin.site.register(Category)
#admin.site.register(Comment)