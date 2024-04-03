import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import glob
# import os

# Initiate analyzer
analyzer = SentimentIntensityAnalyzer()

# Get all paths
diary_paths = glob.glob("diary/*")

# Get date from paths
dates = [diary_path[6:16] for diary_path in diary_paths]
# Perhaps this would be a more correct way to do it? But it seems unnecessary for this program.
# dates = [os.path.splitext(os.path.basename(diary_path))[0] for diary_path in diary_paths]

# Get Data
scores = []
for path in diary_paths:
    with open(path, "r") as file:
        text = file.read()
    scores.append(analyzer.polarity_scores(text))

# Extract Positive and Negative scores
pos_score = [score["pos"] for score in scores]
neg_score = [score["neg"] for score in scores]

# Page
st.title("Tone")

st.subheader("Positivity")
figure = px.line(x=dates, y=pos_score, labels={"x": "Positivity", "y": "Date"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=dates, y=neg_score, labels={"x": "Negativity", "y": "Date"})
st.plotly_chart(figure)
