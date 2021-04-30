import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import json
import requests
import pyjokes



#Speak engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Application Paths
chrome_path = "https://www.google.com/search?q=chrome&oq=chro&aqs=chrome.1.69i65j0i433j0i20i263j69i57j69i60j5l3.8169j0j7&sourceid=chrome&ie=UTF-8"
codePath = '"C:\\Users\\91810\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"'
spotifypath= "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"
News_api = "http://newsapi.org/v2/top-headlines?country=in&apiKey=83cf9663b4424805a128ef57ba3dfdec"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

                
def wishme():
    hour = int(datetime.datetime.now().hour)
    strtime = datetime.datetime.now().strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning Sir! Now the time is ")
        speak(strtime)
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir! Now the time is ")
        speak(strtime)
    else:
        speak("Good Evening Sir! Now the time is !")
        speak(strtime)
        
    speak("I am Jarvis Sir. Please tell me how may I help you")

"""It takes microphone from user and returns string output"""
def takeCommand():  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # our Voice range
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio , language='en-in') # Google engine recognize our voice
        print("You said :",query)
    except:
        print("Say that again Please...")
        return "None" 
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia'in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "quit" in query:
            quit(speak("Ok sir...Good Night! Have a Nice Day! "))

        elif 'open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            try:
                speak("sir , what i search on google")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")
            except:
                speak("opening google")
                webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
            except:
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")
        elif 'open facebook' in query:
            try:
                speak("opening facebook")
                webbrowser.get(chrome_path).open("facebook.com")
            except:
                speak("opening facebook")
                webbrowser.open("facebook.com")


        elif 'play music' in query:
            try:
                os.startfile(spotifypath)
                speak('Playing Music!')
            except:
                speak("Sir Please Install Spotify First!")
                webbrowser.open("https://www.spotify.com/us/")


        elif 'Todays News' in query:
            speak("Todays Top Headlines....Lets Begin")
            news = requests.get(News_api).text
            news_dict = json.loads(news)
                
            arts = news_dict['articles']
            for articles in arts:
                speak(articles['title']) 
                print( articles['title'],'\n')
                print("Click this Link to read =>",articles['url'],'\n') 
                print("IMAGE  => ", articles['urlToImage'],'\n')

                speak("Looking to the next news...Listen Carefully")
            speak("Thanks for listening....")
            if "ok stop" in query:
                quit()

        elif "whats the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the current time is",strtime )

        elif "open vs code"  in query:
            try:
                os.startfile(codePath)
            except:
                speak("Please Install VScode First!")
                webbrowser.get(chrome_path).open("https://code.visualstudio.com//download")

        elif "who made you" in query:
            speak("Dinakar iS the Creator of Me! ")

        elif "Tell me a joke" in query:
            MY_joke = pyjokes.get_joke(language="en",category="neutral")
            speak(MY_joke)

        else:
            speak("Iam not able to Find your Query! Please Tell again")
