
import requests

API_URL = "https://newsapi.org/v2/top-headlines"


def get_news(api_key, speak):
    if not api_key:
        print("Error: API key is missing.")
        speak("News API key is missing.")
        return

    try:
        response = requests.get(
            API_URL,
            params={
                "country": "us",
                "apiKey": api_key
            },
            timeout=10
        )

        print("HTTP Status:", response.status_code)

        response.raise_for_status()
        data = response.json()
        print(data,"this is data ")

        if data.get("status") != "ok":
            print("News API error:", data.get("code"), data.get("message"))
            speak("Unable to fetch news.")
            return

        articles = data.get("articles", [])

        if not articles:
            speak("No news articles found.")
            return

        speak("Here are the top five headlines.")

        for article in articles[:5]:
            title = article.get("title")
            if title:
                print(title)
                speak(title)

    except requests.RequestException as error:
        print("News request error:", error)

        if error.response is not None:
            print("Response details:", error.response.text[:500])

        speak("Unable to fetch news.")

    except ValueError as error:
        print("Invalid news response:", error)
        speak("Unable to read news.")