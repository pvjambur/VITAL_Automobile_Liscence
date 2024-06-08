import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Custom CSS for background
st.markdown(
    """
    <style>
    body {
        background-image: url('background_image.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .title {
        font-family: 'Arial';
        color: #ffffff; /* Text color for title */
    }
    .main {
        background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background color */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title
st.markdown('<h1 class="title">Hackman</h1>', unsafe_allow_html=True)

# Using columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("Enter Details")

    # User inputs
    person_name = st.text_input("Name")
    person_age = st.number_input("Age", min_value=0, max_value=120)
    car_number = st.text_input("Car Number (e.g., KA 05 NC 3452)")
    car_type = st.selectbox("Car Type", ["SUV", "Sedan", "Hatchback"])

with col2:
    st.header("Upload Files")

    # File uploaders
    files_uploaded = st.file_uploader("Upload Photos and Videos", accept_multiple_files=True)

# Submit button
if st.button("Submit"):
    # Generate output based on user inputs
    st.write("Name:", person_name)
    st.write("Age:", person_age)
    st.write("Car Number:", car_number)
    st.write("Car Type:", car_type)

    # Display uploaded files
    for file_upload in files_uploaded:
        if file_upload.type.startswith('image'):
            st.image(file_upload, caption='Uploaded Image', use_column_width=True)
        elif file_upload.type.startswith('video'):
            st.video(file_upload)
