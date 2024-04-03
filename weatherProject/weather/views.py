from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
import json

def weather_microservice(request):
     if request.method == 'GET':
    
        lat_url = request.GET.get('lat', '')
        lon_url = request.GET.get('lon', '')

        try:
            data = json.loads(request.body.decode('utf-8'))
            lat_body = data.get('latitude', '')
            lon_body = data.get('longitude', '')
        except json.JSONDecodeError:
            lat_body = lon_body = ''

        lat = lat_url if lat_url else lat_body
        lon = lon_url if lon_url else lon_body

        API_key = '838bb01ff57bcdd88271651ce0542dc0'

        url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_key

        response = requests.get(url).text

        parsed_data = json.loads(response)

        pretty_json = json.dumps(parsed_data, indent=4)

        print(pretty_json)

        json_data = json.dumps(pretty_json)

        return HttpResponse(pretty_json, content_type='application/json')
     else:
        return HttpResponse(json.dumps({'error': 'Invalid request method'}), content_type='application/json')