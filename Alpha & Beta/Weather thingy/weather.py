# -*- coding: utf-8 -*-
import requests


def get_weather_forecast():
    # Connecting to the weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Krakow&appid=5bf02ce9718e0a2499b758b1c1045b13'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # Parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # Creating our forecast string
    forecast = 'Todays weather is ' + description + ' with a high of '
    forecast += str(int(temp_max)) + ' and a low of '
    forecast += str(int(temp_min)) + '.'

    return forecast
