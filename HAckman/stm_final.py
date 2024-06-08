'''import streamlit as st
import re
# from PIL import Image
import time as t
import speech_recognition as sr

text = ''

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

vehicle_type=st.selectbox("Pick the type of the VEHICLE", ["SUV", "Bike", "asdf"])

vehicle_color=st.color_picker("# color")

data = (f"vehicle number is '{vehicle_number}' ,vehicle type is '{vehicle_type}' and color is '{vehicle_color}'")

st.button("Submit",type="primary")

def inp():
    return data


st.title("Video Upload and Playback")

# Video file uploader

uploaded_file = st.file_uploader("Upload a Image or video file", type=["mp4", "avi", "mov", "mkv","jpg", "jpeg", "png"])

st.text_area("Describe more about vehicle")

# if (st.button("Submit 123")):
#     st.write("HELLO ALL)")

st.markdown("# OUTPUT ")

with st.spinner ("just a moment "):
    t.sleep(2)

# input = st.info(f"vehicle number is '{vehicle_number}' ,vehicle type is '{vehicle_type}' and color is '{vehicle_color}'")


# import streamlit as st

# import pyaudio

# st.title("Voice to Text Converter")

recognizer = sr.Recognizer()


def recognize_speech_from_mic():
    global text
    with sr.Microphone() as source:
        st.sidebar.info("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        st.sidebar.info("Listening... Please speak into the microphone.")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.sidebar.success(f"Recognized Text: {text}")
            return text
        
        
        except sr.RequestError:
            st.sidebar.error("API unavailable")
        except sr.UnknownValueError:
            st.sidebar.error("Unable to recognize speech")

if st.sidebar.button("Start Recording"):
    recognize_speech_from_mic()

st.sidebar.button("submit now")

def inpu():
    return test

if st.button("Submit"):
    inp()

elif st.sidebar.button("submit now") :
    inpu()






# st.balloons()
'''

import streamlit as st
import re
# from PIL import Image
import time as t
import speech_recognition as sr

text = ''

st.markdown("# Crime Detection")

st.image("crime.jpeg", width=600)

# st.balloons()

st.sidebar.title("Welcome to crime detector")
st.sidebar.info("Crime detection system help in finding current information about by taking vehicle details from user")

st.subheader("Enter vehicle number")

pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'  # Example pattern: AA00AA0000
vehicle_number = st.text_input("Enter your vehicle number (e.g., AB12CD3456):")
re.match(pattern, vehicle_number)

st.subheader("Enter vehicle info")

vehicle_type = st.radio("Pick the type of the VEHICLE", ["SUV", "Sedan", "Pickup", "Hatchback","Others"])
# vehicle_color = st.color_picker("Pick the color")
vehicle_color=st.selectbox("Select a color:", ["Red", "Green", "Blue","beige","brown","gold","orange","pink","purple","tan","white","yellow"])

data = f"Vehicle number is '{vehicle_number}', vehicle type is '{vehicle_type}' and color is '{vehicle_color}'"

if st.button("Submit Vehicle Info", key="submit_vehicle_info"):
    st.write(data)

def inp():
    return data

st.title("Video Upload and Playback")

# Video file uploader
uploaded_file = st.file_uploader("Upload an image or video file", type=["mp4", "avi", "mov", "mkv", "jpg", "jpeg", "png"])

if uploaded_file is not None:
    # To read file as bytes:
    video_bytes = uploaded_file.read()

    # Display the video
    st.video(video_bytes)

st.markdown("# OUTPUT")

prompt = st.text_area("Describe more about vehicle")



with st.spinner("Just a moment..."):
    t.sleep(2)

recognizer = sr.Recognizer()

def recognize_speech_from_mic():
    global text
    with sr.Microphone() as source:
        st.sidebar.info("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        st.sidebar.info("Listening... Please speak into the microphone.")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.sidebar.success(f"Recognized Text: {text}")
            return text
        except sr.RequestError:
            st.sidebar.error("API unavailable")
        except sr.UnknownValueError:
            st.sidebar.error("Unable to recognize speech")

if st.sidebar.button("Start Recording", key="start_recording"):
    recognize_speech_from_mic()

def inpu():
    return text

if st.button("Submit", key="submit"):
    inp()
elif st.sidebar.button("Submit Now", key="submit_now"):
    inpu()

st.write(prompt)

# st.balloons()
