# Jarvis-AI-Virtual-Assistant
Jarvis is a  virtual assistant capable of conversation, following basic commands and used to automate your tasks 

![851](https://user-images.githubusercontent.com/77189196/116514535-ca02eb00-a8e8-11eb-9942-eb87876be42d.jpg)

# Project description

## Pyttsx3 

- pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3

- **Installation** :

   ***pip install pyttsx3*** -> [pyttsx3](https://pypi.org/project/pyttsx3/)

   If you recieve errors such as No module named win32com.client, No module named ***win32***, or No module named win32api, you will need to additionally install ***pypiwin32***.

- **Usage** :

  1. import pyttsx3
  2. engine = pyttsx3.init()
  3. engine.say("I will speak this text")
  4. engine.runAndWait()
  
  
## speech_recognition
  8 Library for performing speech recognition, with support for several engines and APIs, online and offline.
  
- **Installation**:

  ***pip install SpeechRecognition***-> [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
  
 - **Usage** :
   1. import speech_recognition as sr
   2. engine = pyttsx3.init('sapi5')
   3. voices = engine.getProperty('voices')
   4. engine.setProperty('voice', voices[0].id)
   5. Recognize speech input from the microphone






