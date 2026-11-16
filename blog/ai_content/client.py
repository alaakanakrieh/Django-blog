from openai import OpenAI
from django.conf import settings

class ContentClient():
    """
    CLIENT LAYER
    The ONLY place in the project that talks to OpenAI.
    It takes a prompt (text) and returns the model's answer (text).
    It knows nothing about posts, the database, or HTTP.
    """
    def __init__(self):
        # self is to do passing for the main key we are use.
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        # API key is in the .env file.

    def generate(self, prompt, system =None):
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
        )   
        return response.choices[0].message.content.strip()
    
# One shared client for the whole project (generate + summarize + future features).
_shared_client = None

def get_content_client():
    """Create the client the first time it is needed, then reuse the same one."""
    global _shared_client
    if _shared_client is None:
        _shared_client = ContentClient()
    return _shared_client
