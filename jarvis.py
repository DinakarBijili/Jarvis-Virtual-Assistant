import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speachRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser  
import os 
import json 
from urllib.request import urlopen
import requests #pip install request
import pyjokes #pip install pyjokes
import subprocess
import wolframalpha # pip install wolframaplha
import warnings
import pywhatkit #pip install pwhatkit
import randfacts # pip install randfacts


warnings.filterwarnings('ignore')

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
        
    speak("hello iam Jarvis 1 point o ")

def username():
    speak('What should i call you')
    name = takeCommand()
    speak("Hello")
    speak(name)

    print("---------------------")
    print("Welcome ",name)
    print("---------------------")
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

# Main function starts here now we will call the functions
if __name__ == "__main__":
    clear = lambda: os.system('cls')
    # This function clear any command before executing of this python file

    clear()
    wishme()
    username()

    while True:
        query = takeCommand().lower()

        if 'jarvis' in query:
            speak("hi am Jarvis 1 point o. How can i help you")
        elif 'hello' in query or 'hi' in query:
            speak("Hello") 
            speak(name) 
            speak("how are you") 
            print(name) 
        
        elif 'Dinakar' in query:
            speak("hello master. How are you")

        elif 'good' in query or 'fine' in query or "iam good" in query:
            speak("Good to here that. Have a great day.")
            
        elif 'change my name to' in query:
            query = query.replace('change my name to',"")
            name = query

        elif 'What is your name' in query or "who are you" in query:
            speak("my name is Jarvis speed 1 terabytz memory 1 zetabytes")

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Thanks for giving me your valuable time. Have a great Day")
            exit()

        elif 'search' in query:
            try:
                query = query.replace('search','')
                webbrowser.open(query)
            except:
                webbrowser.get(chrome_path).open(query)

        elif 'play' in query or 'find' in query:
            song = query.replace('play', '')
            speak('playing song')
            speak(song) 
            pywhatkit.playonyt(song)

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
                webbrowser.open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
                
        
        elif 'open google' in query:
            try:
                speak("what i search on google")
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
            speak("Here we go with music")
            music_dir = "D:\\songs\\english\\Linkin Park"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))

        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                news_dict = json.loads(jsonObj)

                speak("Todays Top Headlines....Lets Begin")
                print("""=========== TIMES OF INDIA ===========""" + '\n')
                
                arts = news_dict['articles']
                for articles in arts:
                    print( articles['title']+'\n')
                    print(articles['description'] + '\n')
                    speak(articles['title']) 
                    
                    print("TO read article =>",articles['url']+'\n') 
                    print("Click to get IMAGE  => ", articles['urlToImage']+'\n')

                    speak("Looking to the next news...Listen Carefully")
                speak("Thanks for listening....")
            except Exception as e:
                if "ok stop" in query:
                    break
                print(str(e))

        elif "Tell me facts" in query:
            x = randfacts.getfact()
            print(x)
            speak(x)
            
        elif "whats the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the current time is",strtime )

        elif "open vs code"  in query:
            try:
                speak("opening vs code")
                os.startfile(codePath)
            except:
                speak("Please Install VScode First!")
                webbrowser.get(chrome_path).open("https://code.visualstudio.com//download")

        elif "who made you" in query:
            speak("I have been Created by Dinakar Bijili")
        
        elif "Where is" in query:
            try:
                query = query.replace("where is","")
                location = query
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
            except:
                webbrowser.get(chrome_path).open("https://www.google.nl/maps/place")
    
        elif "joke" in query or "Tell me a joke" in query:
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
            res = client.query(query)
            try:
                print(next(res.result).text)
                speak(next(res.result).text)
            except StopIteration:
                print("can't able to find your query")
        
         
      
