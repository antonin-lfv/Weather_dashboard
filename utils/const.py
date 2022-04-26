import streamlit as st
from datetime import datetime, timedelta, date

class ConstString:
    SPACE = "##"
    SEPARATOR = "---"


class ConstPageConfig:
    LAYOUT = "wide"
    TITLE = "My app"
    MENU = {
        'About': "My app made with love"
    }


class ConstApi:
    # Air quality
    AIR_QUALITY_CURRENT = "https://air-quality.p.rapidapi.com/current/airquality"
    AIR_QUALITY_24H_HISTORY = "https://air-quality.p.rapidapi.com/history/airquality"
    AIR_QUALITY_FORECAST = "https://air-quality.p.rapidapi.com/forecast/airquality"
    AIR_QUALITY_HEADERS = {
        "X-RapidAPI-Host": "air-quality.p.rapidapi.com",
        "X-RapidAPI-Key": st.secrets["X-RapidAPI-Key"]
    }

    RESPONSE_SUCCES = {'response': 'OK'}
    RESPONSE_FAIL = {'response': 'KO'}


class ConstTime:
    TODAY = datetime.today()
    TODAY_STRING = TODAY.strftime('%Y-%m-%d')


class ConstCoord:
    REIMS_LON = "4.031696"
    REIMS_LAT = "49.258329"
    PARIS_LON = "2.33333"
    PARIS_LAT = "48.866669"


class ConstPath:
    AIR_QUALITY_CURRENT = 'Data/airQuality/current.json'
    AIR_QUALITY_HISTORY = 'Data/airQuality/history.json'
    AIR_QUALITY_FORECAST = 'Data/airQuality/forecast.json'