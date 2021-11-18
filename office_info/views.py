from django.shortcuts import render, get_object_or_404
from .models import Office
import requests
import json


def home(request):
    geek_fact = get_geek_fact()
    if geek_fact:
        geek_fact = geek_fact['joke'].split('.')
    return render(request, 'office_info/homepage.html', {'fact' : geek_fact})

def get_geek_fact():
    joke_data = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    return joke_data.json()

def offices(request):
    offices = get_office_list()
    return render(request, 'office_info/office_select.html', {'offices': offices})

def get_office_list():
    offices = Office.objects.all()
    return offices

def office_info(request):
    office_info = get_office_info(request.GET.get('office'))
    return render(request, 'office_info/office_info.html', {'office':office_info})

def get_office_info(office_id):
    office_info = get_object_or_404(Office, pk=office_id)
    return office_info
