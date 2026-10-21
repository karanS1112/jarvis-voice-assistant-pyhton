
import requests
# this is news API end point
API_URL = "https://newsapi.org/v2/top-headlines"


def get_news(api_key, speak):
    # here is the condition. to check api key in vaialble or n ot 
    if not api_key:
        print("Error: API key is missing.")
        speak("News API key is missing.")
        return

    try:
        #send the get request
        response = requests.get(
            API_URL,
            params={
                "country": "us",
                "apiKey": api_key
            },
            timeout=10
        )
        #this is status code which show in terminal
        print("HTTP Status:", response.status_code)

        response.raise_for_status()
        #get the json response
        data = response.json()
        # chekc the status ! ok throw  error or jarvish speak Unable to fetch news
        if data.get("status") != "ok":
            print("News API error:", data.get("code"), data.get("message"))
            speak("Unable to fetch news.")
            return
        #get the list of  articles
        articles = data.get("articles", [])
        # throw error
        if not articles:
            speak("No news articles found.")
            return
        # here jarvis tell the top five news
        speak("Here are the top five headlines.")
        # itrate the top 5 new get the title 
        for article in articles[:5]:
            title = article.get("title")
            if title:
                print(title)
                speak(title)
    #throw error while exception
    except requests.RequestException as error:
        print("News request error:", error)

        if error.response is not None:
            print("Response details:", error.response.text[:500])

        speak("Unable to fetch news.")

    except ValueError as error:
        print("Invalid news response:", error)
        speak("Unable to read news.")