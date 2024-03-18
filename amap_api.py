# @File     : amap_api.py
# @Time     : 2024/3/17 20:47
# @Author   : Banana
# @Software : PyCharm
# !/usr/bin/env python
# coding: utf-8

import requests

key_xjh = 'da4785b794dc24b6884a49d0975dfecc'


def geo(add: str, city: str) -> dict:
    """获取地理编码"""
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    param = {
        'key': key_xjh,
        'address': add,
        'city': city,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def regeo(location: str) -> dict:
    """获取逆地理编码"""
    url = 'https://restapi.amap.com/v3/geocode/regeo?parameters'
    param = {
        'key': key_xjh,
        'location': location,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def walking(origin: str, destination: str) -> dict:
    """步行路径规划"""
    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    param = {
        'key': key_xjh,
        'origin': origin,
        'destination': destination,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def transit(origin: str, destination: str) -> dict:
    """公交路径规划"""
    url = 'https://restapi.amap.com/v5/direction/transit/integrated?parameters'
    param = {
        'key': key_xjh,
        'origin': origin,
        'destination': destination,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def driving(origin: str, destination: str) -> dict:
    """驾车路径规划"""
    url = 'https://restapi.amap.com/v5/direction/driving?parameters'
    param = {
        'key': key_xjh,
        'origin': origin,
        'destination': destination,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def bicycling(origin: str, destination: str) -> dict:
    """骑行路径规划"""
    url = 'https://restapi.amap.com/v5/direction/bicycling?parameters'
    param = {
        'key': key_xjh,
        'origin': origin,
        'destination': destination,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def distance(origin: str, destination: str) -> dict:
    """测量距离"""
    url = 'https://restapi.amap.com/v3/distance?parameters'
    param = {
        'key': key_xjh,
        'origin': origin,
        'destination': destination,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def place(keywords: str, types: str) -> dict:
    url = 'https://restapi.amap.com/v3/place/text?parameters'
    param = {
        'key': key_xjh,
        'keywords': keywords,
        'types': types,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


def weather(city: str, extensions: str) -> dict:
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    param = {
        'key': key_xjh,
        'city': city,
        'extensions': extensions,
        'output': 'json'
    }
    response = requests.get(url, params=param)
    data = response.json()
    return data


if __name__ == '__main__':
    # res = geo('上海大学', '上海')
    # res = regeo('113.679287,23.632575')
    # res = walking('116.481028,39.989643', '116.434446,39.90816')
    # res = config_district('广州')
    # res = place('广州', '酒店')
    res = weather('上海', 'all')

    print(res)
