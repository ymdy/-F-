import requests
import re
import sys
# coding: utf-8
class Weather():
        
        #引数チェックもそのうち作るよ
    def returnweather(self, day, weat):
        try:
            daylist = ('今日', '明日', '明後日')
            weatherlist = ('晴', '曇' , '雨')
            url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
            query_params = {'city': weat}
            data = requests.get(url, params=query_params).json()
            location = data['location']
            weather = data['forecasts']
            #日付条件分岐
            if re.match(daylist[0], day):
                dayno = 0
            elif re.match(daylist[1], day):
                dayno = 1
            elif re.match(daylist[2], day):
                dayno = 2
            todayweather = weather[dayno]
            todayweatherstr = todayweather['telop']
            #投げる天気情報の絞り込み
            if todayweatherstr.startswith(weatherlist[0]):
                weatherno = weatherlist[0]
            elif todayweatherstr.startswith(weatherlist[1]):
                weatherno = weatherlist[1]
            elif todayweatherstr.startswith(weatherlist[2]):
                weatherno = weatherlist[2]
            else:
                print('取得した天気情報が不明なエラー')
                sys.exit()
            return todayweather['dateLabel'], location['city'], weatherno
        except AttributeError:
            print('エラー！オブジェクトの型が違います。')
        except UnboundLocalError:
            print('エラー！変数に値がありません。')
        except ValueError:
            print('エラー！値が適切ではありません！')
        except:
            print('不明なエラーです。')