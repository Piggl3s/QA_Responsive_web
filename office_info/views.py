from django.shortcuts import render, get_object_or_404
from .models import Office
import requests
import json


# Return HTML views
def get_homepage_view(request):
    geek_fact = get_geek_fact()
    if geek_fact:
        geek_fact = geek_fact['joke'].split('.')
    return render(request, 'office_info/homepage.html', {'fact' : geek_fact})

def get_office_select_view(request):
    offices = get_office_list()
    return render(request, 'office_info/office_select.html', {'offices': offices})

def get_office_information_view(request):
    # Get information about the selected office
    office_info = get_office_info(request.GET.get('office'))
    # update office object with weather information
    office_info.weather = get_local_weather(office_info)
    return render(request, 'office_info/office_info.html', {'office':office_info})


# Homepage functions
def get_geek_fact():
    # Call geek Joke API and return a JSON/Dictionary item
    joke_data = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    return joke_data.json()


# Office select functions
def get_office_list():
    # Return all Offices within the local Database
    offices = Office.objects.all()
    return offices


# Office information functions
def get_office_info(office_id):
    # Retrieve specific office info based off DB id
    office_info = get_object_or_404(Office, pk=office_id)    
    return office_info

def get_office_weather(weather_id):
    # open weather map API Key
    openweathermap_api_key = 'd5bf55428d09f18fb808cf2eb48e52fc'
    # API request passing through specific ID of location
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}".format(weather_id, openweathermap_api_key)).json()
    return weather

def get_local_weather(office_info):
    # Call the weather API with the office weather-id and grab the local weather
    weather = get_office_weather(office_info.openweathermap_id)['weather']

    # create weather info Dict item and icon URL
    weather_information = {}
    weather_icon_url = "http://openweathermap.org/img/wn/{}@2x.png"

    # update Dictionary with todays weather and icon URL
    weather_information["todays_weather"]=weather[0]['main']
    weather_information["weather_icon"] = weather_icon_url.format(weather[0]['icon'])

    # Return weather information
    return weather_information