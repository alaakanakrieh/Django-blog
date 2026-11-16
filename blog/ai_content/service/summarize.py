import logging

from ...models import Post
from .utils import validate_text_input, generate_ai_content

logger = logging.getLogger(__name__)

MAX_SUMMARY_LENGTH = 500

class PostNotFoundError(ValueError):
    """
    Raised when no post has the requested id.
    It IS a ValueError (so it follows the service's error contract),
    but having its own name lets the view return 404 instead of 400.
    """

def _build_summary_prompt(title: str, content: str) -> str:
    """The ONLY place where the summarization prompt is written."""
    return (
        "Summarize the following blog post in 2-3 clear sentences.\n"
        f"Keep the summary under {MAX_SUMMARY_LENGTH} characters.\n"
        "Return only the summary text.\n\n"
        f"Title: {title}\n\n"
        f"Content:\n{content}"
    )

def summarize_post(post_id) -> dict:
    # 1. Validate the input: must be a positive whole number.
    #    (bool is checked because True/False are technically ints in Python)
    if isinstance(post_id, bool) or not isinstance(post_id, int) or post_id <= 0:
        raise ValueError("post_id must be a positive integer.")

    # 2 + 3. Get the post from the database, or raise a clear error.
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise PostNotFoundError(f"Post with id {post_id} does not exist.")

    # 4. Make sure the post actually has text to summarize.
    content = validate_text_input(post.content, min_length=1, field_name="Post content")

    # 5. Build the prompt and call the shared client ONE time.
    prompt = _build_summary_prompt(post.title, content)
    logger.info("Summarizing post %s", post_id)

    # generate_ai_content strips whitespace and raises ValueError
    # if the model returned an empty answer.
    summary = generate_ai_content(prompt)

    # 6. Enforce the 500-character limit even if the model ignores the prompt.
    if len(summary) > MAX_SUMMARY_LENGTH:
        summary = summary[:MAX_SUMMARY_LENGTH].rstrip()

    # 7. Return a predictable dictionary.
    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary),
    }