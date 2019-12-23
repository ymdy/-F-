from Weather import Weather
if __name__ == '__main__':
    locate = ('130010', '140010', '120010') #東京、神奈川、千葉
    selectday = ('今日', '明日', '明後日')
    weather = Weather()
    test = weather.returnweather(selectday[0], locate[0])
    print(test[0] + 'の' + test[1] + 'の天気は' + test[2] + 'です。')