
import webbrowser
#add the url in gictionary for  key and value pair which below i have itrarted the data
WEBSITES = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "instagram": "https://instagram.com",
    "linkedin": "https://linkedin.com",
    "youtube": "https://youtube.com"
}

#this is functon which take the command and send it  boolean value
def open_website(command):
    command = command.lower().strip()
    #this is loop which key and value  mean name and url which opens in webbrowser library
    for name, url in WEBSITES.items():
        if f"open {name}" in command:
            webbrowser.open(url)
            return True

    return False