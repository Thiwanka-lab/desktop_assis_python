import wikipedia
import webbrowser
import os
import streamlit as st

from src.helper import speak, takeCommand, wish_me


"""This is a logic where I can search wikipedia according to the query """
if __name__ == "__main__":
    
    wish_me()

    while True:

    
        st.title("Desktop Assistant")

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
            
        elif "exit" in query:
            speak("Ok sir. Thank you. Bye bye ")
            exit()