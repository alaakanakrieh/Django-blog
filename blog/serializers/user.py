from rest_framework import serializers
from ..models import User # we can write from ..models import Post

class UserSerializer(serializers.ModelSerializer):
    """
    Validates the request body for POST /api/users/ and formats the response.

    What we get for free from the model:
      - username is required and unique  (model: unique=True)
      - email must be a valid email      (model: EmailField)
    """

    class Meta:
        model = User
        # List the fields explicitly so we always know what the API exposes.
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'created_at']
        read_only_fields = ['id', 'created_at']
        # Friendlier error message for a duplicate username.
        extra_kwargs = {
            'username': {
                'error_messages': {'unique': 'A user with this username already exists.'}
            },
        }

    def validate_username(self, value):
        """Custom field validation: runs automatically for the 'username' field."""
        value = value.strip()
        if ' ' in value:
            raise serializers.ValidationError('Username cannot contain spaces.')
        return value