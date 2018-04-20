#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

from utils import API_KEY, LOCATION
now = 'https://api.seniverse.com/v3/weather/now.json'
day = 'https://api.seniverse.com/v3/weather/daily.json'
sug = 'https://api.seniverse.com/v3/life/suggestion.json'

def init():
    location = LOCATION
    global resultNow
    resultNow = getWeather(now,location)
    global resultSug
    resultSug = getWeather(sug,location)
    global resultDay
    resultDay = getWeather(day,location)

def getWeather(mode,location):
    result = requests.get(mode, params={
        'key': API_KEY,
        'location': location,
    }, timeout=1)
    return json.loads(result.text)

def getTemp():
    return resultNow["results"][0]["now"]["temperature"].encode('utf-8')

def getState():
    return resultNow["results"][0]["now"]["text"].encode('utf-8')

if __name__ == '__main__':
    init()
    print resultNow["results"][0]["now"]["text"].encode('utf-8')
    print resultDay["results"][0]["daily"][0]["high"]
    print resultDay["results"][0]["daily"][0]["low"]#最高温度
    print resultDay["results"][0]["daily"][0]["precip"]#降雨概率
    print resultDay["results"][0]["daily"][0]["text_day"].encode('utf-8')
    print resultDay["results"][0]["daily"][0]["text_night"].encode('utf-8')
    print resultSug["results"][0]["suggestion"]["flu"]["brief"].encode('utf-8')
    print resultSug["results"][0]["suggestion"]["sport"]["brief"].encode('utf-8')
    print resultSug["results"][0]["suggestion"]["dressing"]["brief"].encode('utf-8')
