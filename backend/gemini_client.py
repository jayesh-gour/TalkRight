import os
from dotenv import load_dotenv
from google import genai

# loading environment variable from .env
load_dotenv()

# initializing client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# taking response from gemini through user input and system prompt
def get_ai_response(user_input: str, system_prompt: str) -> str:

    full_prompt = f"{system_prompt}\n\nUser: {user_input}"

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=full_prompt
        )

        return response.text


    except Exception as e:
        print(e)
        return "Sorry!, something went wrong. Please try again"