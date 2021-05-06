import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speachRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser # pip install 
import os 
import json 
from urllib.request import urlopen
import requests #pip install request
import pyjokes #pip install pyjokes
import subprocess
import wolframalpha #pip install wolframaplha


#Speak engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# You can change voice Id to 1 to get Female While iam using Male Voice for all text to speach


#Application Paths
chrome_path = "https://www.google.com/search?q=chrome&oq=chro&aqs=chrome.1.69i65j0i433j0i20i263j69i57j69i60j5l3.8169j0j7&sourceid=chrome&ie=UTF-8"
codePath = '"C:\\Users\\91810\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"'
songs = "D:\\songs\\english\\Linkin Park"
News_api = "http://newsapi.org/v2/top-headlines?country=in&apiKey=83cf9663b4424805a128ef57ba3dfdec"
wolframalpha = "WJWQY2-H954L7Y73W"

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
        
    speak("hi am Jarvis Sir Speed 1 terabytz memory 1 zetabytes.")

def username():
    speak('What should i call you sir')
    name = takeCommand()
    speak("Hello Mister")
    speak(name)

    print("#####################")
    print("Welcome ",name)
    print("#####################")
    speak("How can i Help you, Sir")

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
        print("Unable to Recognize your voice. Please Tell Again")
        return "None" 
    return query

# Main function starts here now we will all the functions
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    # This function clear any command before executing of this python file

    clear()
    wishme()
    username()

    while True:
        query = takeCommand().lower()

        if 'jarvis' in query:
            wishme()
            speak("hi am Jarvis Sir Speed 1 terabytz memory 1 zetabytes.")
            
        elif 'change my name to' in query:
            query = query.replace('change my name to',"")
            name = query

        elif 'What is your name' in query or "who are you" in query:
            speak("my name is Jarvis sir speed 1 terabytz memory 1 zetabytes")

        elif 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your valuable time. Have a great Day")
            exit()

        elif 'search' in query or 'play' in query:
            try:
                query = query.replace('search',"")
                query = query.replace('play',"")
                webbrowser.open(query)
            except:
                webbrowser.get(chrome_path).open(query)

        elif 'search in youtube' in query or 'play in youtube' in query:
            try:
                query = query.replace("search in youtube","") 
                query = query.replace("play in youtube","") 
                webbrowser.get("https://www.youtube.com/").open(query)
            except:
                webbrowser.open(query)

        elif 'wikipedia'in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open wikipedia" in query:
            try:
                webbrowser.open("https://www.wikipedia.org/")
            except:
                webbrowser.get(chrome_path).open("https://www.wikipedia.org/")
 
        elif "who i am" in query:
            speak('if you are talking then definatily your human ')

        elif "why you came to world" in query:
            speak("Thanks to Dinakar Bijili. further its a secret")

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

        elif 'play music' in query or 'play songs' in query:
            speak("Here to go with music")
            music_dir = "D:\\songs\\english\\Linkin Park"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))


        elif 'news' in query or 'todays news' in query:
            speak("Todays Top Headlines....Lets Begin")
            try:
                jsonObj = urlopen(News_api)
                news = requests.get(News_api).text
                news_dict = json.loads(news)
                
                arts = news_dict['articles']
                for articles in arts:
                    print( articles['title']+'\n')
                    print(articles['discription'] + '\n')
                    speak(articles['title']) 
                    
                    print("TO read article =>",articles['url']+'\n') 
                    print("Click to get IMAGE  => ", articles['urlToImage']+'\n')

                    speak("Looking to the next news...Listen Carefully")
                speak("Thanks for listening....")
            except Exception as e:
                if "ok stop" in query:
                    break
                print(str(e))
            
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
            speak("I have been Created by Dinakar Bijili  ")
        
        elif "Where is" in query:
            try:
                query = query.replace("where is","")
                location = query
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place" + location + "")
            except:
                webbrowser.get(chrome_path).open("https://www.google.nl/maps/place" + location + "")
    
        elif "Tell me a joke" in query:
            speak(pyjokes.get_joke())

        elif 'shutdown system' in query:
            speak("Hold on a Sec ! Your system on its way to shutdown")
            subprocess.call('shutdown / p /f')
        elif 'restart system' in query:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("What should i write, Sir")
            note = takeCommand()
            file = open("jarvis.txt",'w')
            speak("sir, should i include date and time")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("% I:% M% S %p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show my notes" in query:
            file = open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))
            
        elif "stop" in query:
            break
        
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client(wolframalpha)
            res = clear.query(query)
            try:
                print(next(res.result).text)
                speak(next(res.result).text)
            except:
                print("can't able to find your query")

        else:
            speak("Iam not able to Find your Query! Please Tell again")
