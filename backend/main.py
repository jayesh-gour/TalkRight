from fastapi import FastAPI
from pydantic import BaseModel
from gemini_client import get_ai_response
from prompts import SYSTEM_PROMPT

# object  of fastapi
app = FastAPI()

# pydantic model for input validation
class UserInput(BaseModel):
    user_input: str

# endpoint
@app.post("/chat")
def chat_bot(user_prompt: UserInput):

    response = get_ai_response(user_prompt.user_input, SYSTEM_PROMPT)

    return {"message": response}