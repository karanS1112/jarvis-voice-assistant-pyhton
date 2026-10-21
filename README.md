
# Jarvis Voice Assistant

A Python-based voice assistant that recognizes voice commands
and performs basic tasks.

## Features

- Voice recognition
- Wake word: Hey Jarvis
- Open websites using voice commands
- Play songs from a music library
- Fetch and read top news headlines

## Technologies

- Python
- SpeechRecognition
- PyAudio
- Requests
- subprocess Text-to-Speech,webbrowser

## Requirements

- Python 3
- Microphone access
- Internet connection
- NewsAPI key for news functionality

## Run the project

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Set your NewsAPI key:

```bash
export NEWS_API_KEY="YOUR_API_KEY"
```

Start Jarvis:

```bash
python3 main.py
```

## Usage

Say "Hey Jarvis" and then give a command.

Examples:
- Open Google
- Open YouTube
- Play Swad
- Tell me the news

## Future Improvements

- AI-powered conversations
- More voice commands
- Improved error handling