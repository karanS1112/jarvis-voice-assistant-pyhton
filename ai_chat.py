
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None

chat = None

if client:
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=(
                "You are Jarvis, a friendly personal voice assistant. "
                "Understand the user's question and reply naturally. "
                "Use simple English, keep answers concise, and remember "
                "the context of the current conversation."
            )
        ),
    )


def get_ai_reply(user_text):
    if not chat:
        return (
            "Gemini API key is missing. "
            "Please check your .env file."
        )

    try:
        response = chat.send_message(user_text)
        answer = response.text

        if answer:
            return answer.strip()

        return "Sorry, I could not generate a response."

    except Exception as error:
        # Do not print the API key.
        print("Gemini request failed:", type(error).__name__, str(error))
        return "Sorry, I could not connect to Gemini right now."