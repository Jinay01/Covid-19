from django.shortcuts import render
import json
import requests
from .forms import *
# Create your views here.


def main(request):
    response = requests.get(
        'https://api.covid19api.com/summary')
    ans = response.json()
    answer = ans['Global']
    confirmed = answer['TotalConfirmed']
    recovered = answer['TotalRecovered']
    deaths = answer['TotalDeaths']
    active = confirmed-recovered-deaths
    n_confirmed = answer['NewConfirmed']
    n_recovered = answer['NewRecovered']
    n_deaths = answer['NewDeaths']
    n_active = n_confirmed-n_recovered-n_deaths

    form = CountryInput()
    if request.method == "POST":
        form = CountryInput(request.POST)
        if form.is_valid():
            form.save()
            country = form.cleaned_data["country"]
            return countries(request, country)

    context = {'answer': answer,
               'confirmed': confirmed, 'recovered': recovered, 'deaths': deaths, 'active': active, 'n_confirmed': n_confirmed, 'n_recovered': n_recovered, 'n_deaths': n_deaths, 'n_active': n_active, 'form': form}
    return render(request, 'covid/home.html', context)


def countries(request, country):
    response = requests.get(
        'https://corona.lmao.ninja/v2/countries/' + country + '?yesterday&strict&query%20')
    answer = response.json()
    confirmed = answer['cases']
    recovered = answer['recovered']
    deaths = answer['deaths']
    active = answer['active']
    n_confirmed = answer['todayCases']
    n_recovered = answer['todayRecovered']
    n_deaths = answer['todayDeaths']

    form = CountryInput()
    if request.method == "POST":
        form = CountryInput(request.POST)
        if form.is_valid():
            form.save()
            # country = form.cleaned_data["country"]
            # return countries(request, country)

    context = {'answer': answer, 'country': country,
               'confirmed': confirmed, 'recovered': recovered, 'deaths': deaths, 'active': active, 'n_confirmed': n_confirmed, 'n_recovered': n_recovered, 'n_deaths': n_deaths, 'form': form}
    return render(request, 'covid/countries.html', context)
