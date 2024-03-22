import streamlit as st
import pandas

# Initial Declarations
with open("Files/loremIpsum.txt", 'r') as lp:
    loremIpsum = lp.readline()
data = pandas.read_csv("Exercise4/data.csv")
st.set_page_config(
    layout="wide"
)

# Page
st.title("The Best Company")
st.write(loremIpsum)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, item in data[:4].iterrows():
        st.subheader(f"{item['first name']} {item['last name']}".title())
        st.write(item['role'])
        st.image(f"Exercise4/{item['image']}")

with col2:
    for index, item in data[4:8].iterrows():
        st.subheader(f"{item['first name']} {item['last name']}".title())
        st.write(item['role'])
        st.image(f"Exercise4/{item['image']}")

with col3:
    for index, item in data[8:].iterrows():
        st.subheader(f"{item['first name']} {item['last name']}".title())
        st.write(item['role'])
        st.image(f"Exercise4/{item['image']}")