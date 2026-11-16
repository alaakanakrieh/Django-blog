from rest_framework import serializers
from ..models import Category # we can write from ..models import Category

class CategorySerializer(serializers.ModelSerializer):
    """
    Validates the request body for POST /api/categories/.

    - name is required and unique (model: unique=True)
    """

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'name': {
                'error_messages': {'unique': 'A category with this name already exists.'}
            },
        }

    def validate_name(self, value):
        """
        The database only blocks exact duplicates ("Technology" twice).
        Here we also block "technology" if "Technology" already exists.
        """
        value = value.strip()
        if Category.objects.filter(name__iexact=value).exists():
            raise serializers.ValidationError('A category with this name already exists.')
        return value