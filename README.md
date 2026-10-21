# Jarvis Voice Assistant

## Overview

Jarvis Voice Assistant is a Python-based voice assistant that recognizes voice commands and performs basic tasks. It uses speech recognition to understand user instructions and responds by executing the requested actions.

The assistant can be activated using the wake phrase "Hey Jarvis" and can open websites, play songs from a local music library, and retrieve and read the latest news headlines.

## Features

- Voice recognition for processing spoken commands.
- Wake word detection using "Hey Jarvis".
- Website navigation through voice commands.
- Music playback from a local music library.
- News headline retrieval using the NewsAPI service.
- Text-to-speech functionality for spoken responses.

## Technologies Used

- Python 3
- SpeechRecognition
- PyAudio
- Requests
- subprocess
- webbrowser
- NewsAPI

## Requirements

Before running the project, ensure that you have:

- Python 3 installed on your system.
- A working microphone.
- An active internet connection.
- The required Python dependencies.
- A NewsAPI key for news functionality.
- A compatible text-to-speech utility installed on your system.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Jarvis-Voice-Assistant
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of your Git repository.

### 2. Install Dependencies

Install the required Python packages using the following command:

```bash
python3 -m pip install -r requirements.txt
```

### 3. Configure the NewsAPI Key

Obtain an API key by creating an account at [NewsAPI](https://newsapi.org/).

On macOS, configure the key using:

```bash
export NEWS_API_KEY="YOUR_API_KEY"
```
```

Replace `YOUR_API_KEY` with your actual NewsAPI key. Keep the key private and do not upload it to a public repository.

### 4. Run the Application

Start the voice assistant using:

```bash
python3 main.py
```


## Usage

Once the application is running, say "Hey Jarvis" followed by a supported voice command.

Examples of supported commands:

| Voice Command | Description |
|---|---|
| Open Google | Opens Google in the default web browser. |
| Open YouTube | Opens YouTube in the default web browser. |
| Play Swad | Plays the matching song from the local music library. |
| Tell me the news | Retrieves and reads the latest news headlines. |

The available commands depend on the functionality implemented in the application.

## Error Handling and Troubleshooting

### Microphone Issues

Ensure that your microphone is connected, enabled, and accessible to Python. Check your operating system's microphone permissions if voice recognition does not work.

### Speech Recognition Issues

Speak clearly and minimize background noise. An active internet connection may be required, depending on the speech recognition service being used.

### News Retrieval Issues

Verify that the `NEWS_API_KEY` environment variable is configured correctly. Check your internet connection and API usage limits if news headlines cannot be retrieved.

### Music Playback Issues

Ensure that the requested song exists in the configured music directory and that the application supports its audio format.

### Dependency Installation Issues

Verify that Python and pip are installed correctly. If PyAudio installation fails, consult the installation instructions for your operating system.

## Future Enhancements

- Integration with AI-powered conversational models.
- Support for additional voice commands.
- Improved wake word detection.
- Weather updates and reminders.
- Multilingual voice recognition.
- Enhanced error handling and application logging.

## Security

API keys and other sensitive credentials should be stored in environment variables rather than directly in source code. Never commit secrets to version control.


## Author

Developed as a Python project to explore voice recognition, automation, and speech-based interaction.
