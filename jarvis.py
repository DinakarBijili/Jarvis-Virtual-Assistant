import pyttsx3
import randfacts #pip install pyttsx3
import speech_recognition as sr #pip install speachRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser  
import os 
import json 
from urllib.request import urlopen
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
wolframalphaAPI = "WJWQY2-H954L7Y73W"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
                
def wishme():
    hour = int(datetime.datetime.now().hour)
    strtime = datetime.datetime.now().strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning! Now the time is ")
        speak(strtime)
    elif hour>=12 and hour<18:
        speak("Good Afternoon! Now the time is ")
        speak(strtime)
    else:
        speak("Good Evening! Now the time is !")
        speak(strtime)
        
    speak("hello iam Jarvis 1 point o ")

def username():
    speak('What should i call you')
    name = takeCommand()
    speak("hi..")
    speak(name)

    print("\t=================================")
    print("\t\t Welcome ",name)
    print("\t=================================")
    speak("How can i Help you")

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
        
        if 'jarvis' in query or "hi jarvis" in query:
            speak("hi am Jarvis 1 point o. How can i help you")

        elif 'hello' in query or 'hi' in query:
            speak("Hello! how are you") 

        elif "how are you" in query:
            speak("I am fine, Thank you")

        elif 'dinakar here' in query:
            speak("hello master. How are you")

        elif 'good' in query or 'fine' in query or "iam good" in query:
            speak("Good to here that. Have a great day.")
            
        elif 'change my name to' in query:
            query = query.replace('change my name to',"")
            name = query

        elif 'what is your name' in query or "who are you" in query:
            speak("my name is Jarvis speed 1 terabytz memory 1 zetabytes")

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Thanks for giving me your valuable time. Have a great Day")
            exit()

        elif 'search' in query:
            speak("Searching your query ") 
            query = query.replace('search','')
            try:
                pywhatkit.search(query) 
            except:
                webbrowser.open(query)
                

        elif 'play' in query or 'find' in query:
            song = query.replace('play', '')
            try:
                speak(song) 
                pywhatkit.playonyt(song)
            except:
                speak("Network issue. Check your internet connection") 
        elif 'wikipedia'in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia","")
            try:
                speak("According to Wikipedia")
                results = wikipedia.summary(query, sentences=2)   
                print(results)
                speak(results)
            except:
                webbrowser.open(query)
                

        elif "who i am" in query:
            speak('if you are talking then definatily your human ')

        elif "why you came to world" in query:
            speak("Thanks to Dinakar Bijili. further its a secret")

        elif 'open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
                break
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")
                
        elif 'open google' in query:
            try:
                speak("what should i search on google")
                cm = takeCommand().lower()
                cm = input("\nYou can also Search your query here: ").lower()
                webbrowser.open(f"{cm}")
                break
            except:
                speak("opening google")
                webbrowser.get(chrome_path).open("google.com")


        elif 'open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
                break
            except:
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            try:
                speak("opening facebook")
                webbrowser.get(chrome_path).open("facebook.com")
                break
            except:
                speak("opening facebook")
                webbrowser.open("facebook.com")

        elif 'music' in query or 'songs' in query:
            speak("Here we go with music")
            music_dir = "D:\\songs\\english\\Linkin Park"
            songs = os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=83cf9663b4424805a128ef57ba3dfdec")
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some todays top headlines..lets begin')
                print('''=============== NEWS OF INDIA ============''','\n')
                 
                for article in data['articles']:
                    
                    print(str(i) ,'. ' , article['title'] + '\n')
                    print("description:- ",article['description'] , '\n')
                    print("Read news:- ",article['url']+'\n')
                    speak(article['title'])
                    speak("Looking to the next news...Listen Carefully")
                    i += 1
                speak("Thanks for listening....")
            except Exception as e:
                if "ok stop" in query:
                    break     
                print(str(e))

        elif "tell me facts" in query or "facts" in query:
            x = randfacts.getFact()
            print(x)
            speak(x)

            
        elif "whats the time" in query or "time" in query:
            strtime = datetime.datetime.now().strftime("%H %M %p")
            speak("Sir the current time is")
            speak(strtime)

        elif "open vs code"  in query:
            try:
                speak("opening vs code")
                os.startfile(codePath)
            except:
                speak("Please Install VScode First!")
                webbrowser.get(chrome_path).open("https://code.visualstudio.com//download")


        elif "who made you" in query or "who created you" in query:
            speak("I have been Created by B.Dinakar")
        
        elif "where is" in query:
            try:
                query = query.replace("where is","")
                location = query
                speak("searching your location")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/"+ location+"")
            except:
                webbrowser.get(chrome_path).open("https://www.google.nl/maps/place")
    
        elif "joke" in query or "tell me a joke" in query:
            try:
                speak(pyjokes.get_joke())
            except:
                client = wolframalpha.Client(wolframalphaAPI)
                res = client.query(query)             
                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")

        elif 'shutdown system' in query:
            speak("Hold on a Sec ! Your system on its way to shutdown")
            subprocess.call('shutdown/p/f')

        elif 'restart system' in query:
            subprocess.call(["shutdown", "/r"])

        elif "write a note" in query:
            speak("What should i write, Sir")
            note = takeCommand()
            note = input("Note you can also write: ")
            file = open("jarvis.txt",'w')
            speak("sir, should i include date and time")
            ans = takeCommand()
            ans = str(input())
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%I:%M:%S:%p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show my notes" in query:
            file = open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))
        
        
        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client(wolframalphaAPI)
            res = client.query(query)
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except:
                print ("No results")

        elif "temperature" in query or "todays temperature" in query:
            client = wolframalpha.Client(wolframalphaAPI)
            res = client.query(query)
            try:
                print(next(res.result).text)
                speak(next(res.result).text)
            except:
                print("can't able to find your query")

        elif "calculate" in query:
            client = wolframalpha.Client(wolframalphaAPI)
            res = client.query(query)
            try:
                speak (next(res.results).text)
                print (next(res.results).text) 
            except:
                print ("I can only calculate mathematical problems")

        elif "thanks" in query:
            speak("its my pleasure.")

        elif "stop" in query:
            break

        else:
            query = query.replace(" "," ")
            speak("indeed") 
        
         
      
