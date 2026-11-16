from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.ai_content.service import _generate_post
from blog.models.post import Post


@api_view(['POST'])
def generate_post(request):
    title = request.data.get('title',"")
    tone = request.data.get("tone")

    try:
        result = _generate_post(title, tone)
        post = Post.objects.create(
            title=result["title"],
            content=result["content"],
            author_id=request.data.get("author"),
        )
        result["title_id"] = post.title_id
        return Response(result, status=status.HTTP_201_CREATED)
    except ValueError as exc:
        return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
