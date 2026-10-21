import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import musicLibrary
import requests
import os

recognizer = sr.Recognizer()   
engine = pyttsx3.init()
# https://newsapi.org/ this is url you can create the api key of NEWS
apiKeyNews = os.getenv("NEWS_API_KEY", "")

def speak(text):
    subprocess.run(["say", text], check=True)
    # engine.say(text)
    # engine.runAndWait()

def processCommand(c):
    
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com") 
    elif "open linkdin" in c.lower():
        webbrowser.open("https://linkdin.com")    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    # For music play i have created the music library file: 
    elif c.lower().startswith("play"):
        songs = c.lower().split(" ")[1]
        link=musicLibrary.music[songs]  
        webbrowser.open(link)   
        
    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apiKeyNews}"
        print("test 1")

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("test 2")
            data = response.json()
            articles = data.get("articles", [])
            print("test4",articles)

            for article in articles[:5]:
                title = article.get("title")
                print("test 3")
                if title:
                    print(title)
                    speak(title)
        else:
            print("API Error:", response.status_code)
            speak("Unable to fetch news")
   

       


if __name__ == "__main__":
    speak("Initializing jarvis....")

    while True:
        #listen for the  wake word  "Jarvis"
        r = sr.Recognizer()
        #recognization  speech using sphinx
        print("recognization...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio) 
            print("Recognized:", word)

            if "hey jarvis" in word.lower():
                # print("Wake word detected!")
                speak("yes")  
                # Listen for  one word 
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio) 
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))    
