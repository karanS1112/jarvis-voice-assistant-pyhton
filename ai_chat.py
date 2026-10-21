
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load API keys from the .env file
load_dotenv()

# Get the Gemini API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

# Create the Gemini client only if the API key exists
client = genai.Client(api_key=api_key) if api_key else None

# Initialize chat as None
chat = None

# Create a chat session if the client is available
if client:
    chat = client.chats.create(
        # Select the Gemini model
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
            # Configure Jarvis's behavior and personality
            system_instruction=(
                "You are Jarvis, a friendly personal voice assistant. "
                "Understand the user's question and reply naturally. "
                "Use simple English, keep answers concise, and remember "
                "the context of the current conversation."
            )
        ),
    )

# Function to send the user's question to Gemini and get a reply
def get_ai_reply(user_text):
    if not chat:
        return (
            "Gemini API key is missing. "
            "Please check your .env file."
        )

    try:
        # Send the user's message to Gemini
        response = chat.send_message(user_text)
         # Extract the generated text from the response
        answer = response.text

        if answer:
            return answer.strip()

        return "Sorry, I could not generate a response."

    except Exception as error:
        # Do not print the API key.
        print("Gemini request failed:", type(error).__name__, str(error))
        return "Sorry, I could not connect to Gemini right now."