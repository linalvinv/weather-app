import requests 
from dotenv import load_dotenv
import os
from dataclasses import dataclass
load_dotenv()

#values to be read
@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    humidity: int

#get API key without hardcoding into file
API_key = os.getenv('API_KEY')

def getCoordinates(cityName,stateCode,countryCode,APIkey):
    print("Hi")
    response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={cityName},{stateCode},{countryCode}&appid={APIkey}').json()
    #checks if location exists
    if 'lat' not in response:
        print("Could not find specified coordinates")
        return 999,999
    print(response)
    #return coords
    latitude = response[0].get('lat')
    longitude = response[0].get('lon')
    return (latitude,longitude)

def getWeather(lat, lon, APIkey):
    #use coords to get data of location
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}&units=imperial').json()
    if response.get('cod') != 200:
        return None
    return WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temperature=response.get('main').get('temp'),
        humidity=response.get('main').get('humidity')
    )

def main(city,state,country):
    lat, lon = getCoordinates(city,state,country,API_key)
    #check if location was found
    if lat is 999:
        print("Invalid API call. Ensure information typed is correct.")
        return None
    weatherData = getWeather(lat,lon,API_key)   
    return weatherData
if __name__ == "__main__":
    lat, lon = getCoordinates('Las Vegas','NV','USA',API_key)
    print(getWeather(lat,lon,API_key))