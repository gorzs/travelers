#calls to Google Maps, OpenWeather, Geocoding
import requests
import os
from dotenv import load_dotenv
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_KEY")

def get_route_google(start, end):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {"origin": start, "destination": end, "mode": "driving", "key": GOOGLE_MAPS_KEY}
    response = requests.get(url, params=params)
    return response.ok, response.json()

def get_weather(lat, lon, units="metric"):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units={units}"
    response = requests.get(url)
    return response.ok, response.json()

def get_places_google(lat, lon, radius=3000, place_type="tourist_attraction"):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {"location": f"{lat},{lon}", "radius": radius, "type": place_type, "key": GOOGLE_MAPS_KEY}
    response = requests.get(url, params=params)
    return response.ok, response.json()

def geocode_location(location_name):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": location_name, "key": GOOGLE_MAPS_KEY}
    response = requests.get(url, params=params)
    if response.ok:
        results = response.json().get("results", [])
        if results:
            loc = results[0]["geometry"]["location"]
            return True, (loc["lat"], loc["lng"])
    return False, (None, None)
