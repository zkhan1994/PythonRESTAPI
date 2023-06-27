import requests
from datetime import datetime
user_apid='83d4c9d9903d03a41f1186e450c4aaf9'

apiUrl = 'https://api.openweathermap.org/data/2.5/weather?zip=30144&units=imperial&appid='+user_apid

response = requests.get(apiUrl)
weatherInfo=response.json();
city=weatherInfo['name']
temp=weatherInfo['main']['temp']
windspeed=weatherInfo['wind']['speed']
winddirection=weatherInfo['wind']['deg']
pressure=weatherInfo['main']['pressure']
time=weatherInfo['dt']
time=datetime.fromtimestamp(weatherInfo['dt']) #converts unix time to human readable time   
print('City: ',city)
print('Current Temperature F: ',temp)
print('Wind Speed : ',windspeed)
print('Wind Direction: ',winddirection)
print('Atmospheric Pressure: ',pressure)
print('Time of Report: ',time)