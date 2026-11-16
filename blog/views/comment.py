from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import CommentSerializer


class CommentCreateAPIView(APIView):
    """POST /api/comments/  ->  add a comment to a post."""

    def post(self, request):
        serializer = CommentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    