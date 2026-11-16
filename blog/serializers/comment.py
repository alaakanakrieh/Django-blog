from rest_framework import serializers
from ..models import Comment, User, Post

class CommentSerializer(serializers.ModelSerializer):
    """
    Validates the request body for POST /api/comments/.

    Request body:
        {"content": "Great article!", "author": 1, "post": 1}

    - content is required
    - author must be the id of an existing User
    - post must be the id of an existing Post
    """

    # In the model these are null=True, so we declare them here
    # to make them REQUIRED in the API and to give clear error messages.
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={'does_not_exist': 'Author with id {pk_value} does not exist.'},
    )
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        error_messages={'does_not_exist': 'Post with id {pk_value} does not exist.'},
    )

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']