import requests
import re
class Weather():
        
    def returnweather(self, day, weat):
        daylist = ['今日', '明日', '明後日']
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
        query_params = {'city': weat}
        data = requests.get(url, params=query_params).json()
        location = data['location']
        #print(data['forecasts'])
        weather = data['forecasts']
        if re.match(daylist[0], day):
            dayno = 0
        
        todayweather = weather[dayno]
        
        return todayweather['dateLabel'], todayweather['telop']