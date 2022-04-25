# APIs Docs for this dashboard

---


## I. Air Quality

[Docs](https://rapidapi.com/weatherbit/api/air-quality/)

Reims : {"lon": "4.031696", "lat": "49.258329"}

### A. Current Air quality

Current air quality at {lat, long}

```python
import requests

url = "https://air-quality.p.rapidapi.com/current/airquality"

querystring = {"lon":"-73.00597","lat":"40.71427"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```
<br>

### B. Air quality history

Last 24h of air quality at {lat, long}

```python
import requests

url = "https://air-quality.p.rapidapi.com/history/airquality"

querystring = {"lon":"-78.638","lat":"35.779"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```
<br>

### C. Air quality forecast

Return an x hours air quality forcast at {lat, long}
( Max 72 hours )

```python
import requests

url = "https://air-quality.p.rapidapi.com/forecast/airquality"

querystring = {"lat":"35.779","lon":"-78.638","hours":"72"}

headers = {
	"X-RapidAPI-Host": "air-quality.p.rapidapi.com",
	"X-RapidAPI-Key": config["X-RapidAPI-Key"]
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```
<br>