# import streamlit as st
# import re

# st.title("hackman")

# st.image("crime.jpeg", width = 500)

# st.header("Crime finder")

# st.subheader("Enter vehicle number")

# veh = st.text_input("Enter vehicle no.")



# # st.info("details of car to be searched ")

# st.subheader("Enter vehicle color")

# st.file_uploader("Pick a file")

# st.warning("Criminal found")
# st.success("Done!")
# st.error("data not found")

# st.write ("age")
# st.write(range(95))
# st.markdown(":star:")

# st.checkbox("show")

# st.button("click")

# st.radio("pick intensity",[1,2,3,4])

# st.selectbox("pick any", ["as","asd","asdf"])

# st.select_slider("rating",range(100))


# import streamlit as st
# import re
# # from PIL import Image

# # Set page configuration
# st.set_page_config(layout="wide")

# # Custom CSS
# st.markdown(
#     """
#     <style>
#     .title {
#         font-family: 'Arial';
#         color: #4CAF50;
#     }
#     .main {
#         background-color: #f0f0f5;
#         padding: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )

# st.markdown('<h1 class="title">Hackman</h1>', unsafe_allow_html=True)

# # Using columns for layout
# col1, col2 = st.columns(2)

# with col1:
#     st.image("crime.jpeg")
#     st.header("Crime Finder")
#     st.subheader("Enter details")

#     # Display informational message
#     st.info("Details of person to be searched")

#     # Add inputs for entering details of the person to be searched
#     person_name = st.text_input("Enter the person's name (Not more than 20 letters)")
#     if person_name:
#         letter_count = len(person_name.replace(" ", ""))
#         if letter_count > 20:
#             st.error(f"You have entered {letter_count} letters. Please limit it to just 20 letters.")
#         else:
#             st.success("It is a valid name")

#     person_age = st.number_input("Enter the person's age", min_value=0, max_value=120)
#     person_description = st.text_area("Enter a brief description of the person")

#     # Add a text input for car license number
#     car_license = st.text_input("Enter car license number (Format: ABC-1234)")

#     # Regular expression for license plate format ABC-1234
#     license_pattern = r'^[A-Z]{3}-\d{4}$'

#     if car_license:
#         if re.match(license_pattern, car_license):
#             st.success("Valid license number!")
#         else:
#             st.error("Invalid format! Please enter in the format ABC-1234")

#     # Add a text area for car description with a word limit
#     car_description = st.text_area("Enter car description (max 10 words)")

#     if car_description:
#         word_count = len(car_description.split())
#         if word_count > 10:
#             st.error(f"Too many words! You have entered {word_count} words. Please limit your description to 10 words.")
#         else:
#             st.success("Valid car description!")

# with col2:
#     # Add file uploaders for images and videos
#     image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
#     if image_file is not None:
#         st.image(image_file, caption='Uploaded Image.', use_column_width=True)

#     video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
#     if video_file is not None:
#         st.video(video_file)

# # Additional interactive widgets
# st.checkbox("Show")

# st.button("Click")

# st.radio("Pick intensity", [1, 2, 3, 4])

# st.selectbox("Pick the type of the car you wan", ["", "asd", "asdf"])

# st.select_slider("Rating", range(100))