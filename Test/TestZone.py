# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

with st.expander("Upload file"):
    uploaded_image = st.file_uploader("Upload Image")

if camera_image:
    cimg = Image.open(camera_image)
    gray_camera_img = cimg.convert('L')
    st.image(gray_camera_img)

if uploaded_image:
    uimg = Image.open(uploaded_image)
    gray_uploaded_img = uimg.convert('L')
    st.image(gray_uploaded_img)