
import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

GOOGLE_API_KEY = "AIzaSyBH9SIY2lScbwRY95GWdIzogmQRQoLJokQ"
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


def voice_input():
    # Creating Recognizer instance
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio) # Recognize by google speech recognizer
        print ("you Said :", text)
        return text
    except sr.UnknownValueError:
        print ("Sorry could not understand audio")
    
    except sr.RequestError as e:
        print ("Could not request result from google recognition service;{0}".format(e))     


def text_to_speech(text):
    
    tts = gTTS(text=text, lang ='en') # indicating the using language
    tts.save("speech.mp3") # saving the audio as a mp3 file


def llm_model(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    response= model.generate_content(user_text)
    result = response.text
    return result

# def gen():
#     genai.configure(api_key=GOOGLE_API_KEY)
#     available_models = genai.list_models()  # Hypothetical function
#     for model in available_models:
#         print(model)

