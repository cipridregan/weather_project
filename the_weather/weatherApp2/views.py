from django.shortcuts import render
import requests 
import datetime

# Create your views here.
def index(request):

    if "city" in request.POST:
        city = request.POST["city"]
    else:
        city = "Amsterdam"

    APPID = '2dee8eaf6a1f1ed48a3ca6e61438d225'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid' :APPID, 'units':'metric'}
    try:
        r = requests.get(url=URL, params=PARAMS)
        res = r.json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temperature = res['main']['temp']
        pressure = res['main']['pressure']
        humidity = res['main']['humidity']
        
        day = datetime.date.today()


        return render(request, 'weatherApp2/index.html', {'description' : description, 
        'icon' : icon, 'temperature' : temperature, 'pressure' : pressure,
        'humidity' : humidity, 'day' : day, 'city' : city, 'error': False })
    except:
        return render(request, 'weatherApp2/index.html', { 'description': res['message'], 'erorr': True })
