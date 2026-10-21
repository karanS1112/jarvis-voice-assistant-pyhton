import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import musicLibrary
import requests
import os
from news import get_news
from websites import open_website
from dotenv import load_dotenv
from ai_chat import get_ai_reply

load_dotenv()
recognizer = sr.Recognizer()   
engine = pyttsx3.init()

def speak(text):
    subprocess.run(["say", text], check=True)

apiKeyNews = os.getenv("NEWS_API_KEY")

def processCommand(c):
    
   # here is exit process from jarvis when you say below words it exit from system
    exit_commands = {
        "exit",
        "quit",
        "stop jarvis",
        "bye",
        "goodbye",
        "thank you",
        "thanks",
        "thanks jarvis",
        "thank you jarvis"
    }
    # Here  is the codition for exit
    if c in exit_commands:
        speak("Goodbye! Have a nice day.")
        raise SystemExit
    # This is open website funtion while comand you can open google,linkdin etc link which is mentioned in websites file
    elif open_website(c):
        return

    # THis is music codition  where i have created the dictionary get thename of songs
    elif c.lower().startswith("play"):
        songs = c.lower().split(" ", 1)[1].strip()
        link = musicLibrary.music.get(songs)
    
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found")

    # Fetch news
    elif "news" in c.lower():
        get_news(apiKeyNews, speak)
    # THis is gemini codition where it get the command and pass to get_ai_reply function.
    else:
        answer = get_ai_reply(c)
        speak(answer)    
   

       

if __name__ == "__main__":
    speak("Initializing Jarvis. Say Hey Jarvis to activate me.")

    active = False

    while True:
        try:
            with sr.Microphone() as source:
                if not active:
                    print("Waiting for Hey Jarvis...")
                    audio = recognizer.listen(
                        source, timeout=5, phrase_time_limit=4
                    )

                    word = recognizer.recognize_google(audio)
                    print("Recognized:", word)

                    if "hey jarvis" in word.lower():
                        active = True
                        speak("Yes, I am listening.")
                else:
                    print("Jarvis is active. Speak your command...")
                    audio = recognizer.listen(
                        source, timeout=10, phrase_time_limit=10
                    )

                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand.")

        except sr.RequestError as error:
            print("Speech recognition error:", error)

        except SystemExit:
            break

        except OSError as error:
            print("Microphone error:", error)
