import streamlit as st
import pandas as pd
import plotly.express as px


def get_data(x, y):
    x = x.lower().replace(" ", "_")
    y = y.lower().replace(" ", "_")
    x = df[x]
    y = df[y]
    return x, y


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

x_data, y_data = get_data(x_option, y_option)

# Chart
figure = px.scatter(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)
