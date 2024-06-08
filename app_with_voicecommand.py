import streamlit as st
import speech_recognition as sr
import pyaudio

st.title("Voice to Text Converter")

recognizer = sr.Recognizer()

def recognize_speech_from_mic():
       with sr.Microphone() as source:
           st.info("Adjusting for ambient noise, please wait...")
           recognizer.adjust_for_ambient_noise(source)
           st.info("Listening... Please speak into the microphone.")
           audio = recognizer.listen(source)

           try:
               text = recognizer.recognize_google(audio)
               st.success(f"Recognized Text: {text}")
               return text
           except sr.RequestError:
               st.error("API unavailable")
           except sr.UnknownValueError:
               st.error("Unable to recognize speech")

if st.button("Start Recording"):
       recognize_speech_from_mic()
   

### Explanation