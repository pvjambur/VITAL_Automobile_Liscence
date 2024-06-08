import streamlit as st
import re
from PIL import Image
import time as t

st.markdown("# Crime Detection ")

st.image ("crime.jpeg", width = 500 )

# st.balloons()

st.sidebar.title("Welcome to crime detector")

st.sidebar.info("Crime detection system help in finding current information about by taking vehicle details from user")

st.subheader("Enter vehicle number")

pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'  # Example pattern: AA00AA0000
vehicle_number = st.text_input("Enter your vehicle number (e.g., AB12CD3456):")
re.match(pattern, vehicle_number)

st.subheader("Enter vehicle info")

st.selectbox("Pick the type of the VEHICLE", ["SUV", "Bike", "asdf"])

st.color_picker("# color")

st.title("Video Upload and Playback")

# Video file uploader

uploaded_file = st.file_uploader("Upload a Image or video file", type=["mp4", "avi", "mov", "mkv","jpg", "jpeg", "png"])

st.text_area("Describe more about vehicle")

st.markdown("# OUTPUT ")

with st.spinner ("just a moment "):
    t.sleep(2)


# import streamlit as st
# import speech_recognition as sr
# # import pyaudio

# st.title("Voice to Text Converter")

# recognizer = sr.Recognizer()

# def recognize_speech_from_mic():
#     with sr.Microphone() as source:
#         st.info("Adjusting for ambient noise, please wait...")
#         recognizer.adjust_for_ambient_noise(source)
#         st.info("Listening... Please speak into the microphone.")
#         audio = recognizer.listen(source)

#         try:
#             text = recognizer.recognize_google(audio)
#             st.success(f"Recognized Text: {text}")
#             return text
#         except sr.RequestError:
#             st.error("API unavailable")
#         except sr.UnknownValueError:
#             st.error("Unable to recognize speech")

# if st.button("Start Recording"):
#     recognize_speech_from_mic()
