from rest_framework import viewsets, status
from rest_framework.response import Response
from blog.serializers.user import UserSerializer
from ..models import User
from rest_framework.decorators import APIView, api_view

class UserViewSet(viewsets.ModelViewSet):
    """POST /api/users/  ->  create a new user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view(['POST']) # annotation to specify that this view only accepts POST requests
def create_user(request):
    
    page = int(request.query_params.get('page', 1))
    limit = int(request.query_params.get('limit', 10))
    start = (page - 1) * limit
    end = start + limit
        
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateAPIView(APIView):
    """POST /api/users/  ->  create a new user."""

    def post(self, request):
        # 1. Give the request data to the serializer.
        serializer = UserSerializer(data=request.data)

        # 2. Validate it. If invalid, return the errors with 400.
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # 3. Save to the database and return the new object with 201.
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    