import requests
import PIL

url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
query_params = {'city': '130010'}
data = requests.get(url, params=query_params).json()
location = data['location']
data['image'].show()
print(location['city'])
#print(location['name'])
for weather in data['forecasts']:
        print(weather['dateLabel'] + 'の天気：' + weather['telop'])