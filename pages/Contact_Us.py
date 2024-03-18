import streamlit as st
from Functions.send_email import send_email

with st.form(key="form"):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?",
                         ["Job Inquiries", "Proposals", "Other"])
    message = st.text_area("Your message.")
    email_message = f"""Subject: Contact: {topic} - {user_email}
    
{message}
"""
    button = st.form_submit_button("Submit")

if button:
    print(send_email(email_message))
    st.info("Email sent")
