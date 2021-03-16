import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Application Paths
chrome_path = "https://www.google.com/search?q=chrome&oq=chro&aqs=chrome.1.69i65j0i433j0i20i263j69i57j69i60j5l3.8169j0j7&sourceid=chrome&ie=UTF-8"
codePath = '"C:\\Users\\91810\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening !")
    speak("I am Jarvis Sir. Please tell me how may I help you")

"""It takes microphone from user and returns string output"""
def takeCommand():  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8 # our Voice range
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

        elif "jarvis quit" in query:
            quit(speak("Ok sir...Good Bye Have a Nice Day! "))

        elif 'jarvis open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")
        
        elif 'jarvis open google' in query:
            try:
                speak("opening google")
                webbrowser.get(chrome_path).open("google.com")
            except:
                speak("opening google")
                webbrowser.open("google.com")


        elif 'jarvis open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
            except:
                speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")

        elif 'jarvis play music' in query:
            music_dir = 'D:\\songs\\english\\Linkin Park'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "jarvis whats the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the current time is",strtime )

        elif "jarvis open vs code"  in query:
            try:
                os.startfile(codePath)
            except:
                speak("Please Install VScode First!")
                webbrowser.get(chrome_path).open("https://code.visualstudio.com//download")

        elif "who made you" in query:
            speak("Dinakar IS The Creator of Me! ")


            