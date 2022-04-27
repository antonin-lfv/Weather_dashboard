from utils.classes import *
from utils.const import *
import requests
import streamlit as st
import json


# ===== Air quality

def get_current_airQuality(lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    """From API"""
    url = ConstApi.AIR_QUALITY_CURRENT
    querystring = {"lon": lon, "lat": lat}
    headers = ConstApi.AIR_QUALITY_HEADERS
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def get_last_24hours_airQuality_history(lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    """From API"""
    url = ConstApi.AIR_QUALITY_24H_HISTORY
    querystring = {"lon": lon, "lat": lat}
    headers = ConstApi.AIR_QUALITY_HEADERS
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def get_xhours_airQuality_forecast(x="72", lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    """From API"""
    url = ConstApi.AIR_QUALITY_FORECAST
    querystring = {"lon": lon, "lat": lat, "hours": x}
    headers = ConstApi.AIR_QUALITY_HEADERS
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


def get_current_airQuality_json():
    """From Json"""
    with open(ConstPath.AIR_QUALITY_CURRENT, 'r+') as current:
        data = json.load(current)
        return data


def get_forecast_airQuality_json():
    """From Json"""
    with open(ConstPath.AIR_QUALITY_FORECAST, 'r+') as forecast:
        data = json.load(forecast)
        return data


def get_history_airQuality_json():
    """From Json"""
    with open(ConstPath.AIR_QUALITY_HISTORY, 'r+') as history:
        data = json.load(history)
        return data


def set_current_airQuality(lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    with open(ConstPath.AIR_QUALITY_CURRENT, 'r+') as current:
        data = json.load(current)
        if data["date"] != ConstTime.TODAY_STRING:
            # Update json
            data = get_current_airQuality(lon=lon, lat=lat)
            if 'message' in data.keys():
                return ConstApi.RESPONSE_FAIL
            data["date"] = ConstTime.TODAY_STRING
            # apply update on json
            json.dump(data, open(ConstPath.AIR_QUALITY_CURRENT, "w"), indent=4)
            return ConstApi.RESPONSE_SUCCES


def set_last_24hours_airQuality_history(lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    with open(ConstPath.AIR_QUALITY_HISTORY, 'r+') as history:
        data = json.load(history)
        if data["data"][0]["timestamp_utc"].split("T")[0] != ConstTime.TODAY_STRING:
            # Update json
            data = get_last_24hours_airQuality_history(lon=lon, lat=lat)
            if 'message' in data.keys():
                return ConstApi.RESPONSE_FAIL
            # apply update on json
            json.dump(data, open(ConstPath.AIR_QUALITY_HISTORY, "w"), indent=4)
            return ConstApi.RESPONSE_SUCCES


def set_xhours_airQuality_forecast(x="72", lon=ConstCoord.REIMS_LON, lat=ConstCoord.REIMS_LAT):
    with open(ConstPath.AIR_QUALITY_FORECAST, 'r+') as forecast:
        data = json.load(forecast)
        if data["data"][0]["timestamp_utc"].split("T")[0] != ConstTime.TODAY_STRING:
            # Update json
            data = get_xhours_airQuality_forecast(x=x, lon=lon, lat=lat)
            if 'message' in data.keys():
                return ConstApi.RESPONSE_FAIL
            # apply update on json
            json.dump(data, open(ConstPath.AIR_QUALITY_FORECAST, "w"), indent=4)
            return ConstApi.RESPONSE_SUCCES
