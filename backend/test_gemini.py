from gemini_client import get_ai_response
from prompts import SYSTEM_PROMPT

# Test input
user_message = "How you"

response = get_ai_response(user_message, SYSTEM_PROMPT)

print(response)