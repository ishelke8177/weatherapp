import requests
from django.shortcuts import render


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3725447341da2b87e5cecb32557320d4'

    city_weather = {}

    if request.method == 'GET':
        city = request.GET.get('cityname')

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

    return render(request, 'weather/index.html', {'city_weather' : city_weather})


def about(request):
    return render(request,'weather/about.html')