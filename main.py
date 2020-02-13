# -*- coding: utf-8 -*-
from tocaro_handler import TocaroHandler
from Weather import Weather
from music import Music
from PIL import Image, ImageOps
from io import BytesIO
import urllib.request
import requests
import json
import os
import random

def lambda_handler(title, text, imageurl = 'none'):

    tocaro = TocaroHandler()

    if imageurl == 'none':
        tocaro.set_text(title)
        tocaro.set_color("danger")

        tocaro.set_attachments(
            [
                {
                    "title": 'おすすめの曲',
                    "value": text
                    }
                ]
            )
    else:
        tocaro.set_text(title)
        tocaro.set_color("danger")

        tocaro.set_attachments(
            [
                {
                    "title": 'おすすめの曲',
                    "value": text
                },
                {
                    "image_url": imageurl
                }
            ]
        )

    r = tocaro.send2tocaro()
    return r

def getrandommusic(Weather):#dbからランダムでとってくる処理をなんとなくここに書こうと思って天気を引数に設定してます。
    musiclist = [{'music': '君が代', "artist": '林廣守'}, {'music': 'ゴーストバスター', 'artist': 'Saucy Dog'}, {'music': '瞬き', 'artist': 'Back Number'}, {'music': '津軽海峡冬景色', 'artist': '石川さゆり'}]
    return musiclist[random.randrange(0, len(musiclist)-1)]

def handler(event, context):
    try:
        locate = ('130010', '140010', '120010') #東京、神奈川、千葉
        selectday = ('今日', '明日', '明後日')

        weather = Weather()
        getmusic = Music()

        getedweather = weather.returnweather(selectday[0], locate[0])
        musicinfo = getrandommusic(getedweather[2])

        #ここに天気を渡して、DBからランダムで曲名を取り出す処理を書く
        resultmusic = getmusic.setkeywords(musicinfo['music'], musicinfo['artist'])
        text_header = getedweather[0] + 'の' + getedweather[1] + 'の天気は' + getedweather[2] + 'です。'
        
        if resultmusic[0] == '検索結果0':
            text_subject = musicinfo['artist'] + 'の' + musicinfo['music'] + 'ですが、youtubeの検索で該当しませんでした。'
            lambda_handler(text_header, text_subject)
        else:
            text_subject = resultmusic[0] + 'です。\nURL:https://www.youtube.com/watch?v=' + resultmusic[1]
            lambda_handler(text_header, text_subject, resultmusic[2])

    except UnboundLocalError:
        print('エラー！変数に値がありません。')
    except ValueError:
        print('エラー！値が適切ではありません！')
    except Exception as e:
        print('想定外のエラーです。\n' +  str(e))
    else:
        print('MessagePosted!')
