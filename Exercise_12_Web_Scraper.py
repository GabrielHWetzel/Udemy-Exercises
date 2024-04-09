import requests
import selectorlib
from datetime import datetime
import streamlit as st
import pandas
import plotly.express as px
import sqlite3

URL = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("Exercise12/data.db")


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
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES (?,?)", (now, data))
    connection.commit()


def retrieve():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM temperatures")
    return cursor.fetchall()


def gather_data():
    scrapped = scrape(URL)
    extracted = extract(scrapped)
    store(extracted)


gather_data()

# Plot stuff
date = []
temperature = []
for item in retrieve():
    date.append(item[0])
    temperature.append(item[1])
figure = px.line(x=date, y=temperature, labels={"x": "Dates", "y": "Temperatures"})
st.plotly_chart(figure)
st.button("refresh")
