import requests
import re
import sys
import os
import unicodedata
# coding: utf-8
class Weather():

    def returnweather(self, day, weat):
        try:
            daylist = ('今日', '明日', '明後日')
            weatherlist = ('晴', '曇' , '雨')
            #tocaroからコマンドを受け付けられた場合を想定した処理。
            #引数の値がdaylistと一致しているものをl_inに格納。
            l_in = [s for s in daylist if day in s]
            #l_inの文字数をカウントしてcountに格納。(全角半角を区別するためにあえてunicodedataを使用してます。)
            count = 0
            for c in weat:
                if unicodedata.east_asian_width(c) in 'FWA':
                    count += 2
                else:
                    count += 1
            #引数(dayおよびweat)がルール内に収まっているか判定
            if len(l_in[0]) >= 4 or len(l_in[0]) <= 0 or type(day) != str:
                print('日付変数エラー')
                sys.exit()
            if not str.isdigit(weat) or count != 6 or type(weat) != str:
                print('地域コード変数エラー')
                sys.exit()
            #天気情報のurlを格納。
            url = 'http://weather.livedoor.com/forecast/webservice/json/v1?'
            #引数を使用して天気情報を取得。
            query_params = {'city': weat}
            data = requests.get(url, params=query_params).json()
            #取得したリストデータからlocation(場所)とfrecasts(天気情報等)を抽出。
            location = data['location']
            weather = data['forecasts']

            #日付条件分岐(コマンド機能未実装のため実質いらない)
            if re.match(daylist[0], day):
                dayno = 0
            elif re.match(daylist[1], day):
                dayno = 1
            elif re.match(daylist[2], day):
                dayno = 2
            else:
                print('日付の指定が間違っています。')
                sys.exit()
            #取得した天気情報等を天気状況のみに抽出

            todayweather = weather[dayno]
            todayweatherstr = todayweather['telop']
            #投げる天気情報の絞り込み
            #取得した天気情報の文字列を先頭から比較して、晴・曇・雨の３パターンに分けています。
            if todayweatherstr.startswith(weatherlist[0]):
                weatherno = weatherlist[0]
            elif todayweatherstr.startswith(weatherlist[1]):
                weatherno = weatherlist[1]
            elif todayweatherstr.startswith(weatherlist[2]):
                weatherno = weatherlist[2]
            else:
                print('取得した天気情報が不明なエラー')
                sys.exit()
            #日付・場所・天気情報をreturnで返しています。
            return todayweather['dateLabel'], location['city'], weatherno
        except AttributeError:
            print('エラー！オブジェクトの型が違います。')
        except UnboundLocalError:
            print('エラー！変数に値がありません。')
        except ValueError:
            print('エラー！値が適切ではありません！')
        except:
            print('不明なエラーです。')
