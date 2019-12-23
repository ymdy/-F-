from Weather import Weather
if __name__ == '__main__':
    weather = Weather()
    test = weather.returnweather('今日', '130010')
    print(test[0],test[1])