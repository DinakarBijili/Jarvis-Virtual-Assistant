# Python-AI-Virtual-Assistant
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
  
  
## Speech_Recognition
  8 Library for performing speech recognition, with support for several engines and APIs, online and offline.
  
- **Installation**:

  ***pip install SpeechRecognition***-> [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
  
 - **Usage** :
   1. import speech_recognition as sr
   2. engine = pyttsx3.init('sapi5')
   3. voices = engine.getProperty('voices')
   4. engine.setProperty('voice', voices[0].id)
   5. Recognize speech input from the microphone

## Wolframalpha
Wolframalpha:- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. To install this module type the below command in the terminal.
- **Installation**:
   ***pip install Wolframalpha***-> [Wolframalpha](https://pypi.org/project/wolframalpha/)

 - **Getting API Id** :
  1. Create a account at Wolfram alpha. The account can be created at the [official website](https://account.wolfram.com/auth/create)
  2. After signing up, sign in using your Wolfram ID.
  3. Now you will see the homepage of the website. Head to the section in the top right corner where you see your email. In the drop down menu, select the My Apps (API) option.
  4. Click the Get an AppID button to get the id.
  5. In the next dialog box, give the app a suitable name and description.
  6. Note down the APPID that appears in the next dialog box. This app id will be specific to the application.
  
  ## Subprocess
  - Subprocess:- This module is used for getting system subprocess details which are used in various commands i.e Shutdown, Sleep, etc. This module comes buit-in with Python. 
  
  ## Web browser
  - Web browser:- To perform Web Search. This module comes buit-in with Python. 
  
  ## pyjokes
  - Pyjokes:- Pyjokes is used for collection Python Jokes over the Internet. To install this module type the below command in the terminal.
  **Installation**
  ***pip install pyjokes***-->[pyjokes](https://pypi.org/project/pyjokes/)
  
  ## Datetime
  - Datetime:- Date and Time is used to showing Date and Time. This module comes built-int with Python. 
  
  ## Requests 
  -  Requests: Requests is used for making GET and POST requests. To install this module type the below command in the terminal.
  **Installation**
  ***pip install requests***-->[Requests](https://pypi.org/project/requests/)
  
  
  
  



