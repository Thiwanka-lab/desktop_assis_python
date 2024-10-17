import streamlit as st
from src.helper import llm_model, text_to_speech, voice_input




"""This is a logic create the AI genarated responses """

def main():
    
    
    st.title("AI Assistant Yuhas")
    
    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = llm_model(text)
            text_to_speech(response)


            # Display Text area (Answer), MP3 player and  download link

            # audio_file = open('speech.mp3', 'rb')
            # audio_binary = audio_file.read()

            st.text_area(label="Response:", value=response, height=150)
            #st.audio(audio_binary, format='audio/mp3')
            # #st.download_button(label="Download speech", 
            #                    data=audio_binary,
            #                    file_name="speech.mp3", 
            #                    meme='audio/mp3')




if __name__ == "__main__":
    main()
    
   
    