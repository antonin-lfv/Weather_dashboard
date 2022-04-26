# APIs Docs for this dashboard

---


## I. Air Quality

[Docs](https://rapidapi.com/weatherbit/api/air-quality/)

35 calls / day

### A. Current Air quality

Current air quality at {lat, long}

```python
import requests

url = "https://air-quality.p.rapidapi.com/current/airquality"

querystring = {"lon": "4.031696", "lat": "49.258329"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```

```
lat: Latitude (Degrees).
lon: Longitude (Degrees).
timezone: Local IANA Timezone.
city_name: Nearest city name.
country_code: Country abbreviation.
state_code: State abbreviation/code.
data: [
{

aqi: Air Quality Index [US - EPA standard 0 - +500]
o3: Concentration of surface O3 (µg/m³)
so2: Concentration of surface SO2 (µg/m³)
no2: Concentration of surface NO2 (µg/m³)
co: Concentration of carbon monoxide (µg/m³)
pm25: Concentration of particulate matter < 2.5 microns (µg/m³)
pm10: Concentration of particulate matter < 10 microns (µg/m³)
pollen_level_tree: Tree pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
pollen_level_grass: Grass pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
pollen_level_weed: Weed pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
mold_level: Mold pollen level (0 = None, 1 = Low, 2 = Moderate, 3 = High, 4 = Very High)
-predominant_pollen_type: Predominant pollen type (Trees/Weeds/Molds/Grasses)
}, … ]
```

<br>

### B. Air quality history

Last 24h of air quality at {lat, long}

```python
import requests

url = "https://air-quality.p.rapidapi.com/history/airquality"

querystring = {"lon": "4.031696", "lat": "49.258329"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```

```
lat: Latitude (Degrees).
lon: Longitude (Degrees).
timezone: Local IANA Timezone.
city_name: Nearest city name.
country_code: Country abbreviation.
state_code: State abbreviation/code.
[
{

timestamp_local: Timestamp at local time.
timestamp_utc: Timestamp at UTC time.
ts: Unix Timestamp at UTC time.
aqi: Air Quality Index [US - EPA standard 0 - +500]
o3: Concentration of surface O3 (µg/m³)
so2: Concentration of surface SO2 (µg/m³)
no2: Concentration of surface NO2 (µg/m³)
co: Concentration of carbon monoxide (µg/m³)
pm25: Concentration of particulate matter < 2.5 microns (µg/m³)
pm10: Concentration of particulate matter < 10 microns (µg/m³)
}, … ]
```

<br>

### C. Air quality forecast

Return an x hours air quality forcast at {lat, long}
( Max 72 hours )

```python
import requests

url = "https://air-quality.p.rapidapi.com/forecast/airquality"

querystring = {"lon": "4.031696", "lat": "49.258329","hours":"72"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```

```
lat: Latitude (Degrees).
lon: Longitude (Degrees).
timezone: Local IANA Timezone.
city_name: Nearest city name.
country_code: Country abbreviation.
state_code: State abbreviation/code.
[
{

timestamp_local: Timestamp at local time.
timestamp_utc: Timestamp at UTC time.
ts: Unix Timestamp at UTC time.
aqi: Air Quality Index [US - EPA standard 0 - +500]
o3: Concentration of surface O3 (µg/m³)
so2: Concentration of surface SO2 (µg/m³)
no2: Concentration of surface NO2 (µg/m³)
co: Concentration of carbon monoxide (µg/m³)
pm25: Concentration of particulate matter < 2.5 microns (µg/m³)
pm10: Concentration of particulate matter < 10 microns (µg/m³)
}, … ]
```

<br>