import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



# Taking voice from the system

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)