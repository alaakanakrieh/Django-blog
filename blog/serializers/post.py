from rest_framework import serializers
from ..models import Post, User, Category   
        
class PostSerializer(serializers.ModelSerializer):
    """General serializer used by PostViewSet and get_posts (unchanged)."""

    class Meta:
        model = Post
        fields = '__all__' # This will include all fields of the Post model in the serialized output.
        # fields = ('id', 'title', 'content', 'created_at','updated_at') # This will include only the specified fields in the serialized output (Customization), used whr=en we have security concerns and we don't want to expose all fields of the model.
        read_only_fields = ('title_id',) # field that are read-only and cannot be modified during serialization. In this case.

class PostCreateSerializer(serializers.ModelSerializer):
    """
    Validates the request body for POST /api/posts/.

    Request body:
        {"title": "...", "content": "...", "author": 1, "category": 1}

    - title and content are required (they are required in the model)
    - author must be the id of an existing User
    - category must be the id of an existing Category
    """

    # PrimaryKeyRelatedField checks that the given id exists in the database.
    # If it doesn't, DRF returns a 400 error with the message below.
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        error_messages={'does_not_exist': 'Author with id {pk_value} does not exist.'},
    )

    # The model stores categories as a ManyToMany field ("categories"),
    # but the API receives a single "category" id. write_only=True means
    # it is accepted in the request but not shown in the response.
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        error_messages={'does_not_exist': 'Category with id {pk_value} does not exist.'},
    )

    class Meta:
        model = Post
        fields = ['title_id', 'title', 'content', 'author', 'category', 'categories']
        read_only_fields = ['title_id', 'categories']

    def create(self, validated_data):
        # 1. Take the category out (it is not a real column on Post).
        category = validated_data.pop('category')

        # 2. Create the post with the remaining data (title, content, author).
        post = Post.objects.create(**validated_data)

        # 3. Link the post to the category (ManyToMany).
        post.categories.add(category)
        return post