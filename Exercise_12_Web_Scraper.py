import time
import requests
import selectorlib
from datetime import datetime
import streamlit as st
import pandas
import plotly.express as px

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("Exercise12/extractTemp.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(data):
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("Exercise12/data", 'a') as file:
        file.write(f"{now},{data}\n")


def gather_data():
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    store(extracted)


gather_data()

# Plot stuff
graph_data = pandas.read_csv("Exercise12/data")
figure = px.line(x=graph_data["date"], y=graph_data["temperature"], labels={"x": "Dates", "y": "Temperatures"})
st.plotly_chart(figure)
st.button("refresh")
