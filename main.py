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


# Speech recognition function

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
#text = takeCommand()
#speak(text)

#or
#speak(takeCommand())

"""This is a logic where I can search wikipedia according to the query """
if __name__ == "__main__":
    
    query = takeCommand().lower()
    #print(query)

    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        #print (query)
        result = wikipedia.summary(query, sentences = 2)
        
        speak("according to wikipedia")
        print(result)
        speak(result)