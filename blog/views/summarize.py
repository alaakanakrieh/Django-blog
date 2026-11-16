"""
VIEW LAYER - only HTTP work: read the URL, call the service, return JSON.
No database queries and no prompt building here.
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..ai_content.service import summarize_post, PostNotFoundError

@api_view(["POST"])
def summarize_post_view(request, post_id):
    try:
        result = summarize_post(post_id)
        return Response(result, status=status.HTTP_200_OK)

    # PostNotFoundError must come BEFORE ValueError, because it is a ValueError too.
    except PostNotFoundError as exc:
        return Response({"error": str(exc)}, status=status.HTTP_404_NOT_FOUND)

    except ValueError as exc:
        return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
            