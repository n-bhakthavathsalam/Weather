from django.shortcuts import render, redirect
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST['city']

        # for api key you need https://openweathermap.org/api and then verify your email.
        # wait for some time and then key will be ready use
        API_KEY = '6535c2b29a1467c411c9e9c999e1a2ce'
        
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' 
                    + city + '&appid = API_KEY').read()
        
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else:
        data={}
    return render(request, 'main/index.html', data)
  
