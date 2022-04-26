"""Test API"""

# Historical Air quality

import requests
import streamlit as st

url = "https://air-quality.p.rapidapi.com/history/airquality"

querystring = {"lon": "4.031696", "lat": "49.258329"}

headers = {
    "X-RapidAPI-Host": "air-quality.p.rapidapi.com",
    "X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())