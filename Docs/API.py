# Historical Air quality

import requests
import streamlit as st

url = "https://air-quality.p.rapidapi.com/history/airquality"

querystring = {"lon": "-78.638", "lat": "35.779"}

headers = {
    "X-RapidAPI-Host": "air-quality.p.rapidapi.com",
    "X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
