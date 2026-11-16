from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import CategorySerializer


class CategoryCreateAPIView(APIView):
    """POST /api/categories/  ->  create a new category."""

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)