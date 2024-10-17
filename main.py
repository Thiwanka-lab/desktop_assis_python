import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



# Taking voice from the system

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

#print(voices[1].id)

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 140)

# speak function

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Thiwanka, how are you")

# The Function for greetings using date and time

def wish_me():
    now = datetime.datetime.now()
    hour = now.hour
    if hour >=0 and hour<12:
        speak("Good Morning sir. how may I assist you")

    elif hour >=12 and hour<18:
        speak("Good afternoon sir. how may I assist you")

    else:
        speak("Good evening sir. how may I assist you")


# Speech Recognition function

def takeCommand():
    """This function will recognize voice and return text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:

            print("Recognizing.....")
            query = r.recognize_google(audio, language='en') 
            print(f"user said: {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        
        return query


# takeCommand()

"""Also we can create a logic to speak what i am saying"""
# text = takeCommand()
# speak(text)

#or
#speak(takeCommand())

"""This is a logic where I can search wikipedia according to the query """
if __name__ == "__main__":
    
    wish_me()

    while True:

        query = takeCommand().lower()
        #print(query)

        if "wikipedia" in query:
            query = query.replace("wikipedia","")
            #print (query)
            result = wikipedia.summary(query, sentences = 2)
            
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com") 
        
        elif "github" in query:
            speak("Opening github")
            webbrowser.open("github.com")
            
        elif "goodbye" in query:
            speak("Ok sir. Thank you. Bye bye ")
            exit()