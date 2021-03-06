Jarvis-AI-Virtual-Assistant 🧠 [![](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
============================

![](https://img.shields.io/badge/Python-3.9.0-brightgreen.svg)

![AI](https://user-images.githubusercontent.com/77189196/119809528-d76cbe80-bf02-11eb-80bc-f07eb105b964.jpg)

# Project description
 Jarvis is a  virtual assistant capable of conversation, following basic commands and used to automate your tasks like. 
* Weather forecast. 
* plays multiple files like audio songs and video songs. 
* Tells latest news of India. 
* Open Applications such as Web browsers, text editors, etc
* Finds any Location. 
* Tells jokes and facts.
* it can Search on Wikipedia via voice command.
* Arithmetic Calculations
* shows current calender
* And more... 

 ![skills](https://user-images.githubusercontent.com/77189196/119957903-2167aa00-bfc0-11eb-987f-a406a18ea04c.png)


## Pyttsx3 

- pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3

- **Installation** :   
 `pip install pyttsx3`

   If you recieve errors such as No module named win32com.client, No module named ***win32***, or No module named win32api, you will need to additionally install ***pypiwin32***.

- **Usage** :

  * import pyttsx3
  * engine = pyttsx3.init()
  * engine.say("I will speak this text")
  * engine.runAndWait()
  
  
## Speech_Recognition
  8 Library for performing speech recognition, with support for several engines and APIs, online and offline.
  
- **Installation**:

  `pip install SpeechRecognition`
  
 - **Usage** :
   * import speech_recognition as sr
   * engine = pyttsx3.init('sapi5')
   * voices = engine.getProperty('voices')
   * engine.setProperty('voice', voices[0].id)
   * Recognize speech input from the microphone

## Wolframalpha
Wolframalpha:- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. To install this module type the below command in the terminal.
- **Installation**: 

  `pip install Wolframalpha`

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
 - **Installation**:

   `pip install pyjokes`
  
  ## Datetime
  - Datetime:- Date and Time is used to showing Date and Time. This module comes built-int with Python. 
  
  ## Requests 
  -  Requests: Requests is used for making GET and POST requests. To install this module type the below command in the terminal.
 - **Installation**:

   `pip install requests`
  ## JSON 
  - JavaScript Object Notation (JSON) is a standardized format commonly used to transfer data as text that can be sent over a network. It's used by lots of APIs and Databases, and it's easy for both humans and machines to read. JSON represents objects as name/value pairs, just like a Python dictionary
  
  ## Randfacts
  - Randfacts is a python library that generates random facts. You can use randfacts. getFact() to return a random fun fact.
 - **Installation**:

    `pip install randfacts`
  
  ## OS
  - The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.




