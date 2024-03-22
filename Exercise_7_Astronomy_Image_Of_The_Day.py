import streamlit as st
import requests
import os

# API key from https://api.nasa.gov
api_key = os.getenv("NASA_API_KEY")
url = "https://api.nasa.gov/planetary/apod?"\
    f"api_key={api_key}"

# Get content
response = requests.get(url)
content = response.json()

# Get image
image_url = content["url"]
image_response = requests.get(image_url)
image_path = "Images/iotd.png"
with open(image_path, "wb") as file:
    file.write(image_response.content)

# Content to be used
title = content["title"]
description = content["explanation"]

# Web Page
st.title(title)
st.image(image_path)
st.write(description)

