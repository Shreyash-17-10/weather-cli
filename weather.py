import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("\n===========================")
        print(f"  City    : {data['name']}, {data['sys']['country']}")
        print(f"  Temp    : {data['main']['temp']}°C")
        print(f"  Feels   : {data['main']['feels_like']}°C")
        print(f"  Weather : {data['weather'][0]['description'].title()}")
        print(f"  Humidity: {data['main']['humidity']}%")
        print(f"  Wind    : {data['wind']['speed']} m/s")
        print("===========================\n")
    elif response.status_code == 404:
        print(f"City '{city}' not found!")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city>")
        print("Example: python weather.py Mumbai")
    else:
        city = " ".join(sys.argv[1:])
        get_weather(city)
