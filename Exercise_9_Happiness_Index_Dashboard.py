import streamlit as st
import pandas as pd
import plotly.express as px

# Initial calls
df = pd.read_csv("Files/happy.csv")
options = ("Happiness",
           "GDP",
           "Social Support",
           "Life Expectancy",
           "Freedom to make life choices",
           "Generosity",
           "Corruption")

# Page
st.title("Happiness Index Plot")

x_option = st.selectbox("Select the data for the X-axis", options)
y_option = st.selectbox("Select the data for the Y-axis", options)

st.subheader(f"{x_option} and {y_option}")

# Get data
x_data = df[x_option.lower().replace(" ", "_")]
y_data = df[y_option.lower().replace(" ", "_")]

# Chart
figure = px.scatter(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)
